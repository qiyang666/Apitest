<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="180">
            <FormItem label="配置名称">
                <Input v-model="formItem.name" placeholder="yangyunfei"></Input>
            </FormItem>
            <FormItem label="前台系统用户upk">
                <Input v-model="formItem.upk" placeholder=""></Input>
            </FormItem>
            <FormItem label="erp系统用户名">
                <Input v-model="formItem.username" placeholder="yangyunfei"></Input>
            </FormItem>
            <FormItem label="erp系统（加密后）密码">
                <Input v-model="formItem.password" placeholder="123456"></Input>
            </FormItem>
            <FormItem label="shippingId">
                <Input v-model="formItem.shippingId" placeholder="123456"></Input>
            </FormItem>
            <FormItem>
                <Button type="primary" style="margin-left: 8px" @click="update">更新</Button>
                <Button type="warning" style="margin-left: 8px" @click.native="$router.push('/erpconfig/list')">取消</Button>
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
	      			upk:'',
                    usernaem:'',
                    password:'',
                    shippingId:''
	      		},
	      		erpid:localStorage.getItem('erp_id')
	      	}
      },
      methods:{
			update () {

				this.$ajax.get('/api/erp/update',{
                    params:{
                    	id: this.erpid,
                        name:this.formItem.name,
                        upk:this.formItem.upk,
                        username:this.formItem.username,
                        password:this.formItem.password,
                        shippingId:this.formItem.shippingId
                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0) {
                		this.$router.push('/erpconfig/list')
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
	  		this.$ajax.get('/api/erp/listid',{
                params:{
                	id: this.erpid,
                }
            })
            .then((res) => {
                console.log(res.data)
            	var tmp_ip = ''
            	if(res.data.retcode == 0) {
            		this.formItem.upk = res.data.data.upk
            		this.formItem.name = res.data.data.name
                    this.formItem.username = res.data.data.username
                    this.formItem.password = res.data.data.password
                    this.formItem.shippingId = res.data.data.shippingId
            	}
            })
            .catch(function(error){
                console.log(error)
            });
	  },
    }
</script>