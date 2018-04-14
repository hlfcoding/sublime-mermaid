from os import path
import tempfile, textwrap, webbrowser
import sublime, sublime_plugin

class MermaidViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    title = path.splitext(path.basename(view.file_name() or 'untitled'))[0]
    name = '{0}-{1}-mermaid-view.html'.format(title, view.id())
    pathname = path.join(tempfile.gettempdir(), name)
    selection = view.sel()
    region = selection[0] if selection[0].size() else sublime.Region(0, view.size())
    mermaid = view.substr(region)
    with open(pathname, mode='w', encoding='utf-8') as f:
      f.write(self.html({
        'mermaid': mermaid,
        'settings': sublime.load_settings('mermaid.sublime-settings'),
        'title': title
      }))
    url = 'file://{}'.format(pathname.replace(' ', '%20').replace('(', '%28').replace(')', '%29'))
    webbrowser.get(using='safari').open_new_tab(url)

  def html(self, parameters):
    parameters['mermaid'] = textwrap.indent(parameters['mermaid'], ' ' * 10)
    parameters['quiet_links_style'] = ''
    if parameters['settings'].get('quiet_graph_links'):
      parameters['quiet_links_style'] = textwrap.indent("""
      svg .edgePath:not(:hover) path.arrowheadPath { fill-opacity: 0.3; }
      svg .edgePath:not(:hover) .path { stroke-opacity: 0.3; }
      """, ' ' * 4)
    parameters['theme'] = parameters['settings'].get('theme')
    return textwrap.dedent("""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Mermaid Viewer: %(title)s</title>
        <style>
          .info > * {
            box-sizing: border-box;
            display: inline-block;
            font-size: 1rem;
            margin: 0;
            padding: 0.5rem;
            text-decoration: none;
            white-space: nowrap;
          }
          %(quiet_links_style)s
        </style>
      </head>
      <body style="
        font-family:'system-ui',sans-serif;
        margin:0; overflow:hidden; text-align:center;
      ">
        <div class="info" style="
          background:rgba(255,255,255, 0.8); border:1px solid; font-size:0;
          box-sizing:border-box; height:71px; margin:1rem; position:fixed;
        ">
          <h1 style="border-bottom:1px solid; display:block;">
            <span style="font-weight:normal;">Mermaid Viewer &middot;</span>
            %(title)s
          </h1>
          <a
            href="data:image/svg+xml;base64," download="%(title)s.svg"
            style="border-right:1px solid; width:50%%;"
          >
            Save as SVG
          </a>
          <a
            href="http://svgtopng.com" target="_blank"
            style="width:50%%;"
          >
            Save as PNG
          </a>
        </div>
        <div style="
          box-sizing:border-box; height:100vh; overflow:auto;
          padding-top:calc(71px + 1rem);
        ">
          <div class="mermaid">
%(mermaid)s
          </div>
        </div>
        <script src="https://unpkg.com/mermaid@7.1.2/dist/mermaid.min.js"></script>
        <script>
          mermaid.initialize({
            flowchart: { useMaxWidth: false },
            logLevel: 4,
            theme: '%(theme)s',
          });
          setTimeout(() => {
            document.querySelector('a[download]').href +=
            btoa(document.querySelector('svg').outerHTML);
          }, 1000);
        </script>
      </body>
    </html>
    """ % parameters)
