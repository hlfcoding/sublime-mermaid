# Mermaid (for Sublime)

> :tropical_fish: The missing [Sublime Text 3][] package for [Mermaid][].

[Install Mermaid][] from [Package Control][].

- [x] Flow diagram support, with caveats:
  - Dotted and thick links aren't supported due to their ugliness.
  - Inline node definition isn't supported, plus it does not scale well.
  - `style` isn't supported, since `class` (CSS) support is easier.

![screen-shot](https://user-images.githubusercontent.com/100884/29259374-54e94d34-8077-11e7-91ea-67e92b2ea2d9.png)

```mermaid
graph TB %% tab completion: 'graph'
  ID-1[Node 1] %% tab completion: 'node'
  ID-2>Node 2]
  ID-3(Node 3)
  ID-1---ID-2 %% tab completion: 'link'
  ID-1 --> ID-3
  ID-2--Link between 2 and 3---ID-3
  ID-3-->|Action from 3 to 1|ID-1
  ID-3 -- Action from 3 to 2 --> ID-2
  class ID-1 className %% tab completion: 'class'
  click ID-1 "https://github.com" "Tooltip text" %% tab completion: 'click'
  click ID-2 callback "Tooltip for a callback"
  subgraph A subgraph
    ID-4{Node 4}
    ID-5((Node 5))
    ID-4-->ID-5
  end %% tab completion: 'subgraph'

sequenceDiagram %% tab completion: 'diagram'
  participant A as Alice %% tab completion: 'participant'
  participant B as Bob
  participant C as Carol
  Note left of A: Alice likes to chat %% tab completion: 'note'
  A->B: Hello Bob, how are you? %% tab completion: 'message'
  loop Healthcheck
    B->B: Bob checks himself...
  end %% tab completion: 'loop'
  Note over B: Bob whispers when sick
  alt is sick
    B-->A: Not so good :(
  else is well
    B->A: Feeling fresh like a daisy
  end %% tab completion: 'alt'
  opt Extra response
    B->A: You, Alice?
  end %% tab completion: 'opt'
  Note right of C: Carol is the boss
  C->>A: Get back to work!
  loop Every hour
    A->>B: Request 1
    activate B %% tab completion: 'activate'
    A-x+B: Request 2
    B--x-A: Response 2
    B-->>A: Response 1
    deactivate B
  end
```

- [x] Preview in browser
  - From the Command Palette: `Mermaid: View In Browser`
  - Defaults to the entire file, unless there is a selection.

- [x] Exporting, with caveats:
  - PNG conversion from SVG conflicts with opening file-URL's, so it's a link.
  - Converted SVG may be missing some styling.

![screen-shot](https://user-images.githubusercontent.com/100884/29259302-8ba6ba24-8076-11e7-996c-18cad5df138f.png)

- [ ] Sequence diagram support
- [ ] Gantt diagram support
- [ ] Windows support
- [ ] Linux support

[Sublime Text 3]: http://www.sublimetext.com
[Mermaid]: http://knsv.github.io/mermaid
[Install Mermaid]: https://packagecontrol.io/packages/Mermaid
[Package Control]: https://packagecontrol.io

---

Development:

```sh
# Remove package.
$ my_project_path=~/Projects/sublime-mermaid
$ my_packages_path=~/Library/Application\ Support/Sublime\ Text\ 3/Packages
$ ln -s "$my_project_path" "$my_packages_path/Mermaid"
$ cp "$my_project_path/tests/syntax_test_mermaid.mermaid" "$my_packages_path/Default"
# Develop...
$ rm "$my_packages_path/Default/syntax_test_mermaid.mermaid"
$ rm "$my_packages_path/Mermaid"
# Install package.
```
