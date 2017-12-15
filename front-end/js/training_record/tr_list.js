new Vue({
    el: '#training',
    data: {
        tr_data: [],
        current_url: '',
    },
    mounted() {
        url_obj = window.location;
        this.current_url = url_obj;

        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(url_obj.href)
            .then((cb) => {
                this.tr_data = cb.data;
            })
            .catch((err_cb) => {
                console.log(err_cb);
            });
    },
    methods: {
        detail(seq, membercode) {
            get_cate = this.current_url.pathname;
            category = '/' + get_cate.split('/')[1] + '/detail/' + seq;
            window.location.href = category;

        }
    }

})