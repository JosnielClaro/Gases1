
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
        mostrar: '',
        kword: '',
        transformadores: []
      }
    },
    watch:{
        
        mostrar: function(val) {
          this.Mostrar(val);
        },

        kword: function(val) {
            this.Buscar(val);
        }
    },
    methods:{
        Borrar: function(e){
          e.preventDefault();
           swal({
              title: "Estás seguro?",
              text: "Este objeto no se podrá recuperar",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                swal("Poof! El objeto ha sido eliminado", {
                  icon: "success",
                });
                location.href = e.target.href;
              } else {
                swal("Este objeto está a salvo")
                
              }
            })          
          },
        Mostrar: function(mostrar) {
          var self = this;
          axios.get('/api/mostrar/?kword=' + mostrar)
          .then(function(response){
              self.transformadores=response.data
              console.log(response.data)
          })
          .catch(function(error){
              console.log(error);
          })
      },
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

    