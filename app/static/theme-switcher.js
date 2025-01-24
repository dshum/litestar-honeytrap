let isLight = localStorage.getItem("theme") !== "dark"
const html = document.documentElement
const switchTheme = document.getElementById("theme-switcher")
const moon = "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"pico-color-yellow-150\" width=\"1.2em\" height=\"1.2em\" viewBox=\"0 0 24 24\" stroke-width=\"2\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"></path><path d=\"M12 1.992a10 10 0 1 0 9.236 13.838c.341 -.82 -.476 -1.644 -1.298 -1.31a6.5 6.5 0 0 1 -6.864 -10.787l.077 -.08c.551 -.63 .113 -1.653 -.758 -1.653h-.266l-.068 -.006l-.06 -.002z\" stroke-width=\"0\" fill=\"currentColor\"></path></svg>"
const sun = "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"pico-color-orange-300\" width=\"1.2em\" height=\"1.2em\" viewBox=\"0 0 24 24\" stroke-width=\"2\" fill=\"none\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"></path><path d=\"M12 19a1 1 0 0 1 .993 .883l.007 .117v1a1 1 0 0 1 -1.993 .117l-.007 -.117v-1a1 1 0 0 1 1 -1z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M18.313 16.91l.094 .083l.7 .7a1 1 0 0 1 -1.32 1.497l-.094 -.083l-.7 -.7a1 1 0 0 1 1.218 -1.567l.102 .07z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M7.007 16.993a1 1 0 0 1 .083 1.32l-.083 .094l-.7 .7a1 1 0 0 1 -1.497 -1.32l.083 -.094l.7 -.7a1 1 0 0 1 1.414 0z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M4 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M21 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M6.213 4.81l.094 .083l.7 .7a1 1 0 0 1 -1.32 1.497l-.094 -.083l-.7 -.7a1 1 0 0 1 1.217 -1.567l.102 .07z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M19.107 4.893a1 1 0 0 1 .083 1.32l-.083 .094l-.7 .7a1 1 0 0 1 -1.497 -1.32l.083 -.094l.7 -.7a1 1 0 0 1 1.414 0z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M12 2a1 1 0 0 1 .993 .883l.007 .117v1a1 1 0 0 1 -1.993 .117l-.007 -.117v-1a1 1 0 0 1 1 -1z\" stroke-width=\"0\" fill=\"currentColor\"></path><path d=\"M12 7a5 5 0 1 1 -4.995 5.217l-.005 -.217l.005 -.217a5 5 0 0 1 4.995 -4.783z\" stroke-width=\"0\" fill=\"currentColor\"></path></svg>"

document.addEventListener("DOMContentLoaded", () => {
  html.setAttribute("data-theme", isLight ? "light" : "dark")
  switchTheme.innerHTML = isLight ? sun : moon
  switchTheme.focus()
})

switchTheme.addEventListener("click", (e) => {
  e.preventDefault()
  isLight = !isLight
  html.setAttribute("data-theme", isLight ? "light" : "dark")
  switchTheme.innerHTML = isLight ? sun : moon
  localStorage.setItem("theme", isLight ? "light" : "dark")
})