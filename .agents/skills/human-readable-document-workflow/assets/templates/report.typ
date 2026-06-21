// Minimal Typst report template placeholder.
// Replace this with a production template when Typst becomes the chosen PDF route.

#set document(title: "Report")
#set page(margin: 2.2cm)
#set text(font: "Noto Serif CJK SC", size: 11pt, lang: "zh")

#show heading: it => [
  #set text(weight: "bold")
  #it
]

#show link: underline

#let report(title: "Untitled", body) = [
  #align(center)[#text(size: 18pt, weight: "bold")[#title]]
  #v(1em)
  #body
]
