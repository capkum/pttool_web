Vue.use(VeeValidate, veeConf);


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

new Vue({
    el: '#mbrinfo',
    data: {
        showNotic: false,
        noticStauts: true,
        noticMsg: '',
        mbrData: {
            name: '',
            weight: '',
            height: '',
            sex: 'm',
            activility: 0,
            rhr: '',
            mbr: '',
            mhr: '',
            birthday: '',
            vo2max: '',
            e_mhr: '',
            recovery: 'A',
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
            rt_m: '',
            rt_s: '',
            repeat: 1,
            frequency: '',
            target_time: '',
            types: 'cardio',
        },
        types: [{
            text: 'Cardio',
            value: 'cardio'
        }],
        gender: [{
                text: '남',
                value: 'm'
            },
            {
                text: '여',
                value: 'f'
            }
        ],
        activility: [{
                text: 'Top',
                value: 0
            },
            {
                text: 'High',
                value: 1
            },
            {
                text: 'Medium',
                value: 2
            },
            {
                text: 'Low',
                value: 3
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
    },
    mounted() {
        url_obj = window.location;

        flatpickr.localize(flatpickr.l10ns.ko);
        fp = flatpickr('#birth', {
            wrap: true,
        });

        axios.post(url_obj.href)
            .then((cb) => {
                this.mbrData.name = cb.data.name
                this.mbrData.weight = cb.data.weight,
                this.mbrData.height = cb.data.height,
                this.mbrData.sex = cb.data.sex,
                this.mbrData.activility = cb.data.activility,
                this.mbrData.rhr = cb.data.rhr,
                this.mbrData.mbr = cb.data.mbr,
                this.mbrData.mhr = cb.data.mhr,
                this.mbrData.birthday = cb.data.birthday,
                this.mbrData.vo2max = cb.data.vo2max,
                this.mbrData.e_mhr = cb.data.e_mhr,
                this.mbrData.recovery = cb.data.recovery,
                this.mbrData.intensity_fst = this.data_split(cb.data.intensity)[0],
                this.mbrData.intensity_lst = this.data_split(cb.data.intensity)[1],
                this.mbrData.l1_fst = this.data_split(cb.data.l1)[0],
                this.mbrData.l1_lst = this.data_split(cb.data.l1)[1],
                this.mbrData.l2_fst = this.data_split(cb.data.l2)[0],
                this.mbrData.l2_lst = this.data_split(cb.data.l2)[1],
                this.mbrData.l3_fst = this.data_split(cb.data.l3)[0],
                this.mbrData.l3_lst = this.data_split(cb.data.l3)[1],
                this.mbrData.wt_m = this.format_ms(cb.data.wt)[0],
                this.mbrData.wt_s = this.format_ms(cb.data.wt)[1],
                this.mbrData.it_m = this.format_ms(cb.data.it)[0],
                this.mbrData.it_s = this.format_ms(cb.data.it)[1],
                this.mbrData.ct_m = this.format_ms(cb.data.ct)[0],
                this.mbrData.ct_s = this.format_ms(cb.data.ct)[1],
                this.mbrData.rt_m = this.format_ms(cb.data.rt)[0],
                this.mbrData.rt_s = this.format_ms(cb.data.rt)[1],
                this.mbrData.repeat = cb.data.repeat,
                this.mbrData.frequency = cb.data.frequency,
                this.mbrData.target_time = cb.data.target_time,
                this.mbrData.types = 'cardio'
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

        set_mbrData() {
            this.mbrData['intensity'] = this.mbrData.intensity_fst + '/' + this.mbrData.intensity_lst;
            this.mbrData['l1'] = this.mbrData.l1_fst + '/' + this.mbrData.l1_lst;
            this.mbrData['l2'] = this.mbrData.l2_fst + '/' + this.mbrData.l2_lst;
            this.mbrData['l3'] = this.mbrData.l3_fst + '/' + this.mbrData.l3_lst;
            this.mbrData['wt'] = this.set_min(this.mbrData.wt_m, this.mbrData.wt_s);
            this.mbrData['it'] = this.set_min(this.mbrData.it_m, this.mbrData.it_s);
            this.mbrData['ct'] = this.set_min(this.mbrData.ct_m, this.mbrData.ct_s);
            return this.mbrData;
        },

        onSubmit(crud, e) {
            e.preventDefault();
            axios.defaults.xsrfHeaderName = 'X-CSRFToken';
            url = url_obj.href.replace('read', crud);

            this.$validator.validateAll()
                .then(success => {
                    if (!success) {
                        this.showNotic = true;
                        this.noticStauts = false;
                        this.noticMsg = '입력 항목을 확인 해주세요.';
                        return;
                    }

                    axios.post(url, {
                            mbr_data: this.set_mbrData(),
                        })
                        .then(cb => {
                            this.showNotic = true;

                            if (cb.data == 'True') {
                                this.noticMsg = '정상 수정 되었습니다.';
                                this.noticStauts = true
                            } else {
                                this.noticMsg = '정상적으로 입력되지 않았습니다.';
                                this.noticStauts = false;
                            }
                            setTimeout(function () {
                                this.showNotic = false;
                            }.bind(this), 20000);
                        })
                        .catch(err_cb => {
                            console.log(err_cb);
                            return cb.data = false;
                        });
                });

        }

    }
})