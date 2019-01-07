<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="80">
			<FormItem label="域名">
	            <Input v-model="formItem.url" placeholder="http://www.secoo.com"></Input>
	        </FormItem>
	        <FormItem label="对应IP">
	            <Input v-model="formItem.ip" placeholder="192.168.3.1,192.168.3.2"></Input>
	        </FormItem>
	        <FormItem>
	            <Button type="primary" style="margin-left: 8px" @click="save">保存</Button>
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
	      	}
      },
      methods:{
			save () {

				this.$ajax.get('/api/ipconfig/create',{
                    params:{
                        url:this.formItem.url,
                        ip:this.formItem.ip,
                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0){
                		this.$router.push('/ipconfig/list')
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