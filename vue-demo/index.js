// Vue.component 必须执行在 new Vue 之前
Vue.component('comment', {
    props: ['comment'],
    template: '<li>{{comment.content}}</li>'
});

var app = new Vue({
    el: '#app',
    methods: {
        logMessage() {
            console.log(this.message);
            this.message += ' click button';
            this.welcome_show = !this.welcome_show;
        }
    },
    data: {
        message: 'hello',
        title: 'ghello',
        welcome_if: true,
        welcome_show: false,
        comments: [{
                content: 'nice...'
            },
            {
                content: 'great...'
            },
            {
                content: 'brilliant...'
            },
            {
                content: 'awesome...'
            }
        ]
    }
});