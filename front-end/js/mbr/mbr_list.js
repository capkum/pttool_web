Vue.component('mbrmodal', {
    template: `
    <transition name="fade">
        <div class="modal is-active">
            <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title"> \${mbrInfo.name} 님 </p>
                    <button class="delete" aria-label="close" @click="$emit('close')"></button>
                </header>
                <section class="modal-card-body">
                    <p class="columns" style="margin: 10px, 0;">
                        <span class="button is-info is-fullwidth" @click="go_url(mbrInfo.membercode, 'members/read')"> Cardio Data </span>
                    </p>
                    <p class="columns" style="margin: 10px, 0;">
                        <span class="button is-info is-fullwidth"  @click="go_url(mbrInfo.membercode, 'cardio')"> Cardio Program </span>
                    </p>
                    <p class="columns" style="margin: 10px, 0;">
                        <span class="button is-info is-fullwidth" @click="go_url(mbrInfo.membercode, 'training_record')"> Training Record </span>
                    </p>
                    <p class="columns" style="margin: 10px, 0;">
                        <span class="button is-info is-fullwidth"> Inbody </span>
                    </p>
                </section>
                <footer class="modal-card-foot">
                </footer>
            </div>
        </div>
    </transition>
    `,
    props: ['mbrInfo'],
    methods: {
        go_url(membercode, uri) {
            window.location.href = '/' + uri + '/' + membercode
        }
    }
});

let user = new Vue({
    el: '#mbrList',
    data: {
        mbrData: [],
        moment: moment,
        search: '',
        showModal: false,
        modal_conf: {
            name: '',
            membercode: '',
        },
    },
    mounted() {
        url_obj = window.location;
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(url_obj.href)
            .then((cb) => {
                this.mbrData = cb.data;
            })
            .catch((err_cb) => {
                console.log(err_cb);
            });
    },
    computed: {
        filteredList() {
            return this.mbrData.filter(cb => {
                searchNm = this.search.toLowerCase();
                return cb.fields.name.toLowerCase().indexOf(searchNm) > -1;
            });
        }

    },
    methods: {
        modal(name, membercode) {
            this.showModal = true;
            this.modal_conf.name = name;
            this.modal_conf.membercode = membercode;
        },
    }
});