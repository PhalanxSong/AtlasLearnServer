const express = require('express');
const eventRouter = require('./routes/eventRouter');
const app = express();

// port 首选 node 环境变量中 port 默认值
// 如果没有设置 则 使用 3000
//const port = process.env.PORT || 3000
const port = 3000

app.use('/api', eventRouter);

app.get('/', (req, res) => {
    res.send('hello');
});

app.listen(port, () => console.log(`监听端口 ： ${port}`));