new Vue({
    el: '#mbrinfo',
    data: {
        current_url: '',
        mbrDetail: []
    },
    mounted() {
        url_obj = window.location;
        this.current_url = url_obj;

        flatpickr.localize(flatpickr.l10ns.ko);
        fp = flatpickr('#birth', {
            wrap: true,
        });

        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(url_obj.href)
            .then((cb) => {
                this.mbrDetail = cb.data[0];
            })
            .catch((err_cb) => {
                console.log(err_cb);
            });
    },
})