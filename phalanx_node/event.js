var events = require('events');
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