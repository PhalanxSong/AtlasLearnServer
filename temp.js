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