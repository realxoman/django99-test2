const Karim = {
    data(){
        return{
            logo_fixed: false
        }
    },methods: {
        ax_fixed_logo(){
            this.logo_fixed = !this.logo_fixed
        }
    },
}

const vm = Vue.createApp(Karim).mount('#axapp')
