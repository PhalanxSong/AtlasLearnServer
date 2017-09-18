db.albums.updateOne({
    title: "18 and life"
}, {
    $set: {
        artist: "Skid Row"
    }
})

// 查找文档并限制返回的字段
// 查找 year 为 1994 的 全部文档
// 输出 title year 字段
// 不输出 _id 字段
db.movies.find({
    year: 1994
}, {
    title: 1,
    year: 1,
    _id: 0
})

// 输出 符合条件的文档 的 数量
db.movies.find({}, {
    title: 1,
    year: 1,
    "rating.averange": 1,
    _id: 0
}).size()

// 限制查询 10 个文档 并 跳过 前 5 个文档 输出
db.movies.find({}, {
    title: 1,
    year: 1,
    "rating.averange": 1,
    _id: 0
}).limit(10).skip(5)

// 以 rating.averange 降序排列
// -1 为 升序排列
db.movies.find({}, {
    title: 1,
    year: 1,
    "rating.averange": 1,
    _id: 0
}).sort({
    "rating.averange": 1
})

// 查询操作符 $gt $lt 等
db.movies.find({
    "rating.averange": {
        $gt: 9.5
    }
}, {
    title: 1,
    "rating.averange": 1,
    _id: 0
})

// 查询操作符：包含与不包含 - $in 与 $nin 
db.movies.find({
    genres: {
        $in: ["犯罪", "剧情"]
    }
}, {
    title: 1,
    genres: 1,
    _id: 0
})


const jwt = require('jsonwebtoken');

// 默认签名算法 HS256 对称算法 签发和验证使用相同密码

// 创建与签发
const payload = {
    name: 'PhalanxSong',
    admin: true
};
const secret = 'I_LOVE_PHALANXSONG';
const token = jwt.sign(payload, secret);
console.log(token);

// 验证与解码
jwt.verify(token, secret, (error, decoded) => {
    if (error) {
        console.log(error.message);
        return;
    }
    console.log(decoded);
});

// RS256 非对称算法 使 签发和验证使用不同密码
// private key & public key

// 生成私钥
ssh - keygen - t rsa - b 2048 - f private.key
// 生成公钥
openssl rsa - in private.key - pubout - outform PEM - out public.key
// 删除中间文件
rm - rf private.key.pub

const jwt = require('jsonwebtoken');
const fs = require('fs');

// 创建与签发
const payload = {
    name: 'PhalanxSong',
    admin: true
};
const privateKey = fs.readFileSync('./config/private.key');
const token = jwt.sign(payload, privateKey, {
    algorithm: 'RS256'
});
console.log(token);

// 验证与解码
const publicKey = fs.readFileSync('./config/public.key');
jwt.verify(token, publicKey, (error, decoded) => {
    if (error) {
        console.log(error.message);
        return;
    }
    console.log(decoded);
});