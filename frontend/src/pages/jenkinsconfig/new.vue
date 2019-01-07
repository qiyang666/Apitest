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
	            <Input v-model="formItem.taskdescribe"type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="描述jenkins任务" ></Input>
	        </FormItem>

	        <FormItem>
	            <Button type="primary" style="margin-left: 8px" @click="save">保存</Button>
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
	      	}
      },
      methods:{
			save () {

				this.$ajax.get('/api/jenkinsconfig/create',{
                    params:{
                        name:this.formItem.name,
                        taskdescribe:this.formItem.taskdescribe,

                    }
                })
                .then((res) => {
                	if(res.data.retcode == 0){
                		this.$router.push('/jenkinsconfig/list')
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
