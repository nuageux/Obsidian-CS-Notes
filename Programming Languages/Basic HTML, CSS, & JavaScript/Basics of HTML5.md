#HTML #Practical
# HTML
"HyperText Markup Language".
- "HyperText" is text that contains links to other texts.
- "Markup" is the annotation to tell the browser or machine what the content is.

For **structure**.

## HTML Tags
```html
<opening tag> [content] </closing tag>
```

## Standard HTML Document Template
```html
<!DOCTYPE html>
<html>
	<head>
		<!-- describes the main content of the page. -->
		<!-- a.k.a. metadata. -->
		<!-- <meta> will communicate info to the browser. -->
		<meta charset="utf-8"> <!-- the most common character set. -->
		<title>This is required.</title>
	</head>
	<body>
		Anything works here.
		<p>Or make it a paragraph!</p>
	</body> 
</html>
```
- Note that HTML is compiled/rendered sequentially, from top to bottom.

Block-level elements begin on a new line and can contain inline or other block-level elements.
- `<div></div>` is the most common block-level element.
- "Flow" content

Inline elements begin on the same line and may only contain other inline elements.
- `<span></span>` is the most common inline element.
- "Phrasing" content

We need to escape certain special characters.
- Instead of `<`, use `&lt;`
- `>` $\rightarrow$ `&gt;`
- `&` $\rightarrow$ `&amp;`
- Copyright symbol $\rightarrow$ `&copy;`
- If we don't want a certain phrase to split when the page wraps: `&nbsp;` (non-breaking space)

### Useful Tags
**Images**
- `<img src="link" width="number" height="number" alt="description of image for the visually impaired">`
- Doesn't require a closing tag.
- Width and height attributes tell the browser to reserve some space so the page doesn't "jump" while loading. Use them.

### Linking
When linking, set the `target` attribute of the `<a>` tag to `_blank` in order to open the link in a new tab or new window.

**Fragment Identifiers**
- Points to sections of the current page.
- `href="#[name]"`
	- Where `name` is set in the `id` attribute to `[name]` in any tag.
