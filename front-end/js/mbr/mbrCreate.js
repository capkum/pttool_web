new Vue({
    el: '#mbrCreate',
    data: {
        mbrData: {
            name: '',
            weight: 0,
            height: 0,
            sex: 'm',
            activility: 0,
            rhr: 0,
            e_mhr: 0,
            recovery: 'A',
            intensity_fst: 0,
            intensity_lst: 0,
            l1_fst: 0,
            l1_lst: 0,
            l2_fst: 0,
            l2_lst: 0,
            l3_fst: 0,
            l3_lst: 0,
            wt_m: 0,
            wt_s: 0,
            it_m: 0,
            it_s: 0,
            ct_m: 0,
            ct_s: 0,
            repeat: 1,
            frequency: 0,
            target_time: 0,
            types: 'cardio',
        },
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
    }
})