Vue.component('notic', {
    template: `
    <transition name="fade">
        <div class="notification">
            <button class="delete" aria-label="close" @click="$emit('close')"></button>
            \${msg}
        </div>
    </transition>
    `,
    props: ['msg']
});

t1 = new Vue({
    el: '#mbrinfo',
    data: {
        current_url: '',
        mbrDetail: [],
        showNotic: false,
        noticStauts: true,
        noticMsg: '',
        activility: [{
                text: 'Top',
                value: '0'
            },
            {
                text: 'High',
                value: '1'
            },
            {
                text: 'Medium',
                value: '2'
            },
            {
                text: 'Low',
                value: '3'
            },
        ],
        recovery: [{
                text: 'A(13이상)',
                value: 'A'
            },
            {
                text: 'B(8이상 12이하)',
                value: 'B'
            },
            {
                text: 'C(7이하)',
                value: 'C'
            },
        ],
        gender: [{
                text: '남',
                value: 'm'
            },
            {
                text: '여',
                value: 'f'
            }
        ],
        intensity_fst: '',
        intensity_lst: '',
        l1_fst: '',
        l1_lst: '',
        l2_fst: '',
        l2_lst: '',
        l3_fst: '',
        l3_lst: '',
        wt_m: '',
        wt_s: '',
        it_m: '',
        it_s: '',
        ct_m: '',
        ct_s: '',
        types: 'cardio',

    },
    mounted() {
        url_obj = window.location;
        this.current_url = url_obj;

        flatpickr.localize(flatpickr.l10ns.ko);
        fp = flatpickr('#birth', {
            wrap: true,
        });

        axios.defaults.xsrfHeaderName = "X-CSRFToken";
        axios.post(url_obj.href)
            .then((cb) => {
                this.mbrDetail = cb.data;
                this.intensity_fst = this.data_split(this.mbrDetail.intensity)[0];
                this.intensity_lst = this.data_split(this.mbrDetail.intensity)[1];
                this.l1_fst = this.data_split(this.mbrDetail.l1)[0];
                this.l1_lst = this.data_split(this.mbrDetail.l1)[1];
                this.l2_fst = this.data_split(this.mbrDetail.l2)[0];
                this.l2_lst = this.data_split(this.mbrDetail.l2)[1];
                this.l3_fst = this.data_split(this.mbrDetail.l3)[0];
                this.l3_lst = this.data_split(this.mbrDetail.l3)[1];
                this.wt_m = this.format_ms(this.mbrDetail.wt)[0];
                this.wt_s = this.format_ms(this.mbrDetail.wt)[1];
                this.it_m = this.format_ms(this.mbrDetail.it)[0];
                this.it_s = this.format_ms(this.mbrDetail.it)[1];
                this.ct_m = this.format_ms(this.mbrDetail.ct)[0];
                this.ct_s = this.format_ms(this.mbrDetail.ct)[1];
            })
            .catch((err_cb) => {
                console.log(err_cb);
            });
    },
    methods: {
        data_split(val) {
            return (val || '').split('/')
        },
        format_ms(min) {
            if (min < 60) {
                return ['00', min];

            } else {
                set_min = min / 60;
                set_sec = min % 60;
                min = (set_min < 10) ? '0' + set_min : set_min;
                sec = (set_sec < 10) ? '0' + set_sec : set_sec;

                return [min, sec];
            }
        },
        set_min(min, sec) {
            sec = parseInt(sec);
            min = (parseInt(min) > 0) ? parseInt(min) * 60 : 0;
            return min + sec;
        },
        onSubmit(crud) {
            mbrData = {}
            mbrData['name'] = this.mbrDetail.name;
            mbrData['weight'] = this.mbrDetail.weight;
            mbrData['height'] = this.mbrDetail.height;
            mbrData['birthday'] = this.mbrDetail.birthday;
            mbrData['rhr'] = this.mbrDetail.rhr;
            mbrData['e_mhr'] = this.mbrDetail.e_mhr;
            mbrData['vo2max'] = this.mbrDetail.vo2max;
            mbrData['mhr'] = this.mbrDetail.mhr;
            mbrData['frequency'] = this.mbrDetail.frequency;
            mbrData['repeat'] = this.mbrDetail.repeat;
            mbrData['intensity'] = this.intensity_fst + '/' + this.intensity_lst;
            mbrData['l1'] = this.l1_fst + '/' + this.l1_lst;
            mbrData['l2'] = this.l2_fst + '/' + this.l2_lst;
            mbrData['l3'] = this.l3_fst + '/' + this.l3_lst;
            mbrData['wt'] = this.set_min(this.wt_m, this.wt_s);
            mbrData['it'] = this.set_min(this.it_m, this.it_s);
            mbrData['ct'] = this.set_min(this.ct_m, this.ct_s);
            mbrData['types'] = this.types;
            mbrData['sex'] = this.mbrDetail.sex;
            mbrData['recovery'] = this.mbrDetail.recovery;
            mbrData['activility'] = this.mbrDetail.activility;

            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = 'X-CSRFToken';
            url = url_obj.href.replace('read', crud);

            axios.post(url, {
                    mbr_data: mbrData
                })
                .then((cb) => {
                    this.showNotic = true;

                    if (cb.data == 'True') {
                        this.noticMsg = '정상 수정 되었습니다.';
                        this.noticStauts = true
                    } else {
                        this.noticMsg = '오류가 발생하였습니다.';
                        this.noticStauts = false;
                    }
                    setTimeout(function () {
                        this.showNotic = false;
                    }.bind(this), 20000);
                })
                .catch((err_cb) => {
                    console.log(err_cb);
                });
        }

    }
})