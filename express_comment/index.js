const express = require('express');
const morgan = require('morgan');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();

// port 首选 node 环境变量中 port 默认值
// 如果没有设置 则 使用 3000
//const port = process.env.PORT || 3000
const port = 3000;

// 输出日志中间件
app.use(morgan('dev'));

app.use(bodyParser.urlencoded({
    extended: false
}));

let comments = [];
app.locals.comments = comments;

app.set('views', path.resolve(__dirname, 'views'));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/comments', (req, res) => {
    res.render('comments/index');
});

app.get('/comments/new', (req, res) => {
    res.render('comments/new');
});

app.post('/comments/new', (req, res) => {
    if (!req.body.comment) {
        res.status(400).send('Do you have something to say ?');
        return;
    }
    comments.push({
        comment: req.body.comment,
        create_at: new Date()
    })
    res.redirect('/comments');
});

app.listen(port, () => console.log(`监听端口 ： ${port}`));