## Basics
```js
import React from 'react'
import ReactDOM from 'react-dom'

// yadda yadda

ReactDOM.render({JSX element}, document.getElementById('app'))
```



# JSX
Is HTML within JavaScript.
```jsx
const myExample = (
	<div className="major-div">
		<p>And thas wassup</p>
		<p>{10 * 10}*</p>    <!-- shows 100 -->
	</div>
)
```
- Note that each JSX expression may only contain one outermost HTML element and is wrapped in parentheses.
- If you want JavaScript expressions to compile within a JSX expression, surround with curly braces.
- Use "className" as the class attribute in JSX.

```JSX
const aList = (
	<ul>
		{age > 15 && <li>Roller Coaster!</li>}
	</ul>
)
```
- Note that using the && operator with the intention of using its short-circuiting properties lets us selectively choose which elements to show.
- Don't use conditionals in JSX unless they are ternary or &&. Use the conditionals outside the JSX and pass them in.

```JSX
<!-- an event listener example -->
const handleClick = () => alert("Hello world")
const button = <button onClick={handleClick}>Click 
									    Me!</button>
```

```JSX
<!-- common JSX technique -->
const strings = ['Home', 'Shop', 'About Me']
const listItems = strings.map(s => <li>{s}</li>)
<ul>{listItems}</ul>
```

