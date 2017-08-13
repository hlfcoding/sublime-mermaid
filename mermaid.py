from os import path
import tempfile, textwrap, webbrowser
import sublime, sublime_plugin

class MermaidViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    title = path.splitext(path.basename(view.file_name() or 'untitled'))[0]
    name = '%s-%s-mermaid-view.html' % (title, view.id())
    pathname = path.join(tempfile.gettempdir(), name)
    selection = view.sel()
    region = selection[0] if selection[0].size() else sublime.Region(0, view.size())
    mermaid = view.substr(region)
    with open(pathname, mode='w', encoding='utf-8') as f:
      f.write(self.html({ 'mermaid': mermaid, 'title': title }))
    url = "file://%s" % pathname.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    webbrowser.get(using='safari').open_new_tab(url)

  def html(self, parameters):
    return textwrap.dedent("""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Mermaid Viewer: %(title)s</title>
        <link rel="stylesheet" href="https://unpkg.com/mermaid@7.0.3/dist/mermaid.min.css">
      </head>
      <body style="font-family:'system-ui',sans-serif; text-align:center;">
        <h1>Mermaid Viewer: %(title)s</h1>
        <div style="overflow:auto;">
          <div class="mermaid">
          %(mermaid)s
          </div>
        </div>
        <script src="https://unpkg.com/mermaid@7.0.3/dist/mermaid.min.js"></script>
        <script>
          mermaid.initialize({ logLevel: 4 });
        </script>
      </body>
    </html>
    """ % parameters)
