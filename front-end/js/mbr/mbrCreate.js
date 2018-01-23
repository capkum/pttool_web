Vue.use(VeeValidate, veeConf);

Vue.component('comfirmModal', {
    template: `
    <transition name="fade">
        <div class="modal is-active">
            <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title"> 경고 </p>
                    <button class="delete" aria-label="close" @click="$emit('close')"></button>
                </header>
                <section class="modal-card-body">
                    \${msg}
                </section>
                <footer class="modal-card-foot">
                    <button class="button" @click="$emit('close')"> 취소 </button>
                    <button class="button is-danger" @click="goUrl($event)"> 확인 </button>
                </footer>
            </div>
        </div>
    </transition>
    `,
    props: ['msg'],
    methods: {
        goUrl(event) {
            event.preventDefault();
            window.location.href = '../create/';
        }
    }
});

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
    el: '#mbrCreate',
    data: {
        showModal: false,
        showNotic: false,
        noticStauts: true,
        noticMsg: '',
        modalMsg: '',
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
        flatpickr.localize(flatpickr.l10ns.ko);
        fp = flatpickr('#birth', {
            wrap: true,
        });
    },
    methods: {
        formReset(crud, event) {
            this.showModal = true;
            this.modalMsg = '작성한 데이터는 삭제됩니다.';
        },
        set_min(min, sec) {
            sec = parseInt(sec);
            min = (parseInt(min) > 0) ? parseInt(min) * 60 : 0;
            return min + sec;
        },
        onSubmit(crud, e) {
            e.preventDefault();
            this.$validator.validateAll()
                .then(success => {
                    if (!success) {
                        return
                    }
                });
            mbrData = {}
            mbrData['name'] = this.mbrData.name;
            mbrData['weight'] = this.mbrData.weight;
            mbrData['height'] = this.mbrData.height;
            mbrData['birthday'] = this.mbrData.birthday;
            mbrData['rhr'] = this.mbrData.rhr;
            mbrData['e_mhr'] = this.mbrData.e_mhr;
            mbrData['vo2max'] = this.mbrData.vo2max;
            mbrData['mhr'] = this.mbrData.mhr;
            mbrData['frequency'] = this.mbrData.frequency;
            mbrData['repeat'] = this.mbrData.repeat;
            mbrData['intensity'] = this.mbrData.intensity_fst + '/' + this.mbrData.intensity_lst;
            mbrData['l1'] = this.mbrData.l1_fst + '/' + this.mbrData.l1_lst;
            mbrData['l2'] = this.mbrData.l2_fst + '/' + this.mbrData.l2_lst;
            mbrData['l3'] = this.mbrData.l3_fst + '/' + this.mbrData.l3_lst;
            mbrData['rt'] = this.set_min(this.mbrData.rt_m, this.mbrData.rt_s);
            mbrData['wt'] = this.set_min(this.mbrData.wt_m, this.mbrData.wt_s);
            mbrData['it'] = this.set_min(this.mbrData.it_m, this.mbrData.it_s);
            mbrData['ct'] = this.set_min(this.mbrData.ct_m, this.mbrData.ct_s);
            mbrData['type'] = this.mbrData.types;
            mbrData['sex'] = this.mbrData.sex;
            mbrData['recovery'] = this.mbrData.recovery;
            mbrData['activility'] = this.mbrData.activility;

            axios.defaults.xsrfHeaderName = 'X-CSRFToken';
            axios.post(`../${crud}/`, {
                    mbr_data: mbrData
                })
                .then((cb) => {
                    this.showNotic = true;

                    if (cb.data == 'True') {
                        this.noticMsg = '정상 등록 되었습니다.';
                        this.noticStauts = true
                    } else {
                        this.noticMsg = '오류가 발생하였습니다.';
                        this.noticStauts = false;
                    }
                    setTimeout(function () {
                        this.showNotic = false;
                        window.location = '../../';
                    }.bind(this), 5000);
                })
                .catch((err_cb) => {
                    console.log(err_cb);
                });
        }
    }
});
