# Mermaid (for Sublime)

> :tropical_fish: The missing [Sublime Text 3][] package for [Mermaid][].

[Install Mermaid][] from [Package Control][].

- [x] Flow diagram support, with caveats:
  - Dotted and thick links aren't supported due to their ugliness.
  - Inline node definition isn't supported, plus it does not scale well.
  - `--` isn't supported, since `---` is more conventional.
  - `style` isn't supported, since `class` (CSS) support is easier.

![screen-shot](https://user-images.githubusercontent.com/100884/29259374-54e94d34-8077-11e7-91ea-67e92b2ea2d9.png)

```mermaid
graph TB %% tab completion: 'graph'
  ID-1[This is the text in the box] %% tab completion: 'node'
  ID-2[This is the text in the box]
  ID-1---ID-2 %% tab completion: 'link'
  click ID-1 "http://www.github.com" "Tooltip for a link" %% tab completion: 'click'
  subgraph This is the subgraph text
    ID-3[This is the text in the box]
    ID-2-->ID-3
  end %% tab completion: 'subgraph'

graph BT %% tab completion: 'graph'
  ID-1>This is the text in the asymmetric box] %% tab completion: 'node'
  ID-2>This is the text in the asymmetric box]
  ID-1 --> ID-2 %% tab completion: 'link'
  click ID-1 callback "Tooltip for a callback" %% tab completion: 'click'
  class ID-1 className %% tab completion: 'class'

graph TD %% tab completion: 'graph'
  ID-1(This is the text in the rounded box) %% tab completion: 'node'
  ID-2(This is the text in the rounded box)
  ID-1---This is the link text---ID-2 %% tab completion: 'link'

graph LR %% tab completion: 'graph'
  ID-1{This is the text in the rhombus} %% tab completion: 'node'
  ID-2{This is the text in the rhombus}
  ID-1-->|This is the link text|ID-2 %% tab completion: 'link'

graph RL %% tab completion: 'graph'
  ID-1((This is the text in the circle)) %% tab completion: 'node'
  ID-2((This is the text in the circle))
  ID-1 --- This is the link text --> ID-2 %% tab completion: 'link'

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
