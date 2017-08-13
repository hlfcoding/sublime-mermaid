# Mermaid (for Sublime)

> :tropical_fish: The missing [Sublime Text 3][] package for [Mermaid][].

```mermaid
%% Example code
graph BT
  ID-1[This is the text in the box] %% tab completion: 'node'
  ID-2[This is the text in the box]
  ID-1---ID-2 %% tab completion: 'link'
  click ID-1 callback "Tooltip for a callback"
  class ID-1 className
  subgraph This is the subgraph text
    ID-3[This is the text in the circle]
    ID-1-->ID-3
  end

%% Example code
graph TB
  ID-1>This is the text in the asymmetric box] %% tab completion: 'node'
  ID-2>This is the text in the asymmetric box]
  ID-1 --> ID-2 %% tab completion: 'link'
  click ID-1 "http://www.github.com" "This is a tooltip for a link"

%% Example code
graph TD
  ID-1(This is the text in the rounded box) %% tab completion: 'node'
  ID-2(This is the text in the rounded box)
  ID-1---This is the link text---ID-2 %% tab completion: 'link'

%% Example code
graph LR
  ID-1{This is the text in the rhombus} %% tab completion: 'node'
  ID-2{This is the text in the rhombus}
  ID-1-->|This is the link text|ID-2 %% tab completion: 'link'

%% Example code
graph RL
  ID-1((This is the text in the circle)) %% tab completion: 'node'
  ID-2((This is the text in the circle))
  ID-1 --- This is the link text --> ID-2 %% tab completion: 'link'
```

[Sublime Text 3]: http://www.sublimetext.com
[Mermaid]: http://knsv.github.io/mermaid
