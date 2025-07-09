+++
title = "Markdown Cheatsheet (INTERNAL HUGO GUIDANCE)"
hidden = true
+++

From <https://mcshelby.github.io/hugo-theme-relearn/authoring/markdown/>

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!INFO]
> Information that users <ins>_might_</ins> find interesting.

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!primary] There may be pirates
> It is all about the boxes.

> [!secondary] There may be pirates
> It is all about the boxes.

> [!accent] There may be pirates
> It is all about the boxes.

{{% notice style="primary" title="Primary" %}}
A **primary** disclaimer
{{% /notice %}}



{{% notice style="secondary" title="Secondary" %}}
A **secondary** disclaimer
{{% /notice %}}

{{% notice style="accent" icon="stopwatch" %}}
An **accent** disclaimer
{{% /notice %}}

> [!tip] Callouts can have custom titles
> Like this one.

> [!tip] Title-only callout

> [!note]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed

> [!note]+ Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed


```mermaid {align="center" zoom="true"}
graph LR;
  If --> Then
  Then --> Else
```
https://mermaid.js.org/syntax/flowchart.html


<!-- attachments -->
{{% resources style="primary" expanded="false" /%}}

{{< tabs title="hello." >}}
{{% tab title="py" %}}
```python
print("Hello World!")
```
{{% /tab %}}
{{% tab title="sh" %}}
```bash
echo "Hello World!"
```
{{% /tab %}}
{{% tab title="c" %}}
```c
printf"Hello World!");
```
{{% /tab %}}
{{< /tabs >}}

{{% tree %}}
- home | folder
  - [.config](http://example.com) | folder
  - My Documents | folder | magic
    - home.php | fa-fw fab fa-php | #888cc4
{{% /tree %}}

