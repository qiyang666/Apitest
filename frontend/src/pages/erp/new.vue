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
	            <Button type="primary" style="margin-left: 8px" @click="save">保存</Button>
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
	      			username:'',
	      			password:'',
	      			shippingId:''
	      		},
	      	}
      },
      methods:{
			save () {

				this.$ajax.get('/api/erp/create',{
                    params:{
                        name:this.formItem.name,
                        upk:this.formItem.upk,
                        username:this.formItem.username,
                        password:this.formItem.password,
                        shippingId:this.formItem.shippingId
                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0){
                		this.$router.push('/erpconfig/list')
                	}else if(res.data.retcode == 1){
                		this.$Notice.error({
	                        title: '名称不能重复',
	                    });
                	}else{
                		this.$Notice.error({
	                        title: '添加失败',
	                    });
                	}
                })
                .catch(function(error){
                    console.log(error)
                });

			}
	  }
    }
</script>