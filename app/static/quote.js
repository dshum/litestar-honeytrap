const ws = new WebSocket("/random-quote")
const displayQuote = (quote, author) => {
  const element = document.getElementById("quote")
  element.querySelector("blockquote > span").innerText = quote
  element.querySelector("blockquote > footer > cite").innerText = author
}

ws.onmessage = async (event) => {
  const {quote, author} = JSON.parse(event.data)

  if (quote && author) {
    displayQuote(quote, author)
  }
}

fetch("/random-quote")
  .then(response => response.json())
  .then(({quote, author}) => {
    displayQuote(quote, author)
  })
