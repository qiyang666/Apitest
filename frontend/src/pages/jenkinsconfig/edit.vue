<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="180">
            <FormItem label="任务名称">
                <Input v-model="formItem.name" placeholder="jenkins任务名称"></Input>
            </FormItem>
            <FormItem label="任务描述">
                <Input v-model="formItem.taskdescribe" placeholder="任务描述"></Input>
            </FormItem>

            <FormItem>
                <Button type="primary" style="margin-left: 8px" @click="update">更新</Button>
                <Button type="warning" style="margin-left: 8px" @click.native="$router.push('/jenkinsconfig/list')">取消</Button>
            </FormItem>
        </Form>
	</div>
</template>
<script>

    export default {

      data () {
	      	return {
	      		index:1,
	      		formItem:{
	      			name:'',
	      			taskdescribe:''
	      		},
	      		erpid:localStorage.getItem('erp_id')
	      	}
      },
      methods:{
			update () {

				this.$ajax.get('/api/jenkinsconfig/update',{
                    params:{
                    	id: this.erpid,
                        name:this.formItem.name,
                        taskdescribe:this.formItem.taskdescribe

                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0) {
                		this.$router.push('/jenkinsconfig/list')
                	}else{
                		this.$Notice.error({
	                        title: '更新失败',
	                    });
                	}
                })
                .catch(function(error){
                    console.log(error)
                });
			}
	  },
	  mounted:function() {
	  		this.$ajax.get('/api/jenkinsconfig/listid',{
                params:{
                	id: this.erpid,
                }
            })
            .then((res) => {
                console.log(res.data)
            	var tmp_ip = ''
            	if(res.data.retcode == 0) {
            		this.formItem.taskdescribe = res.data.data.taskdescribe
            		this.formItem.name = res.data.data.name

            	}
            })
            .catch(function(error){
                console.log(error)
            });
	  },
    }
</script>
