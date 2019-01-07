<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="80">
			<FormItem label="域名">
	            <Input v-model="formItem.url" placeholder="输入域名"></Input>
	        </FormItem>
	        <FormItem label="对应IP">
	            <Input v-model="formItem.ip" placeholder="输入IP地址"></Input>
	        </FormItem>
	        <FormItem>
	            <Button type="primary" style="margin-left: 8px" @click="update">更新</Button>
	            <Button type="warning" style="margin-left: 8px" @click.native="$router.push('/ipconfig/list')">取消</Button>
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
	      			url:'',
	      			ip:''
	      		},
	      		ipid:localStorage.getItem('ipid')
	      	}
      },
      methods:{
			update () {

				this.$ajax.get('/api/ipconfig/update',{
                    params:{
                    	id: this.ipid,
                        url:this.formItem.url,
                        ip:this.formItem.ip,
                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0) {
                		this.$router.push('/ipconfig/list')
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
	  		this.$ajax.get('/api/ipconfig/listid',{
                params:{
                	id: this.ipid,
                }
            })
            .then((res) => {
            	var tmp_ip = ''
            	if(res.data.retcode == 0) {
            		this.formItem.url = res.data.data.url
            		this.formItem.ip = res.data.data.iplist
            	}
            })
            .catch(function(error){
                console.log(error)
            });
	  },
    }
</script>