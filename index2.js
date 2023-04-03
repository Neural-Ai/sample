const React = require('react')
const ReactDOMServer = require('react-dom/server')
const ReactMarkdown = require('react-markdown')


const express = require('express')
const app = express()

const React = require('react')
const ReactDOMServer = require('react-dom/server')
const ReactMarkdown = require('react-markdown')

const port = 3000

const markdownContent = '# Hello, world!'

app.get('/', (req, res) => {
  const html = ReactDOMServer.renderToString(
    React.createElement(ReactMarkdown, {source: markdownContent})
  )

  res.send(html)
})

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`)
})
