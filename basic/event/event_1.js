// 引入 events 模块
var events = require('events');
// 创建 eventEmitter 对象
var eventEmitter = new events.EventEmitter();

// 创建事件处理程序
var connectHandler = function connected() {
	console.log('连接成功。');

	// 触发 data_received 事件 
	eventEmitter.emit('data_received');
}

// 绑定 connection 事件处理程序
eventEmitter.on('connection', connectHandler);

// 使用匿名函数绑定 data_received 事件
eventEmitter.on('data_received', function () {
	console.log('数据接收成功。');
});

// 触发 connection 事件 
eventEmitter.emit('connection');

eventEmitter.on('delay_event', function () {
	console.log('delay_event 事件触发');
});

eventEmitter.on('some_event', function (arg1, arg2) {
	console.log('listener1', arg1, arg2);
});
eventEmitter.on('some_event', function (arg1, arg2) {
	console.log('listener2', arg1, arg2);
});

eventEmitter.emit('some_event', 'arg1 参数', 'arg2 参数');

setTimeout(function () {
	eventEmitter.emit('delay_event');
}, 1000);

// 类继承形式
class Player extends events.EventEmitter { }

var player = new Player();

player.on('play', (track) => {
    console.log(`On 正在播放：《${track}》`);
});

player.emit('play', '極樂凈土');
player.emit('play', '海阔天空');

player.once('play_once', (track) => {
    console.log(`Once 正在播放：《${track}》`);
});

player.emit('play_once', '極樂凈土');
player.emit('play_once', '海阔天空');

console.log("程序执行完毕。");