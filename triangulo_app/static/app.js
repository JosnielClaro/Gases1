const { createApp } = Vue

  createApp({
    delimiters: ['{$', '$}'],
    created(){
        axios.get('/api/buscar/')
        .then(response => this.transformadores = response.data);
    },
    data() {
      return {
        message: 'Hello ',
        kword: '',
        transformadores: []
      }
    },
    watch:{
        kword: function(val) {
            this.Buscar(val);
        }
    },
    methods:{
        Buscar: function(kword) {
            var self = this;
            axios.get('/api/buscar/?kword=' + kword)
            .then(function(response){
                self.transformadores=response.data
                console.log(response.data)
            })
            .catch(function(error){
                console.log(error);
            })
        }

    }
  }).mount('#app')