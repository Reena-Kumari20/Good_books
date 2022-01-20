const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
  res.json({"Reena":50})
})
app.get('/about', (req, res) => {
      res.json({"Reena":50})
    })

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})