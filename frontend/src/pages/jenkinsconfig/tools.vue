<style scoped>
	 @import './index.css';
</style>
<template>
	<div class="case-zone">
		<Form :model="formItem" :label-width="140">
			<!-- <h1>选择任务</h1> -->
			<FormItem label="选择任务">
	            <Select v-model="model1">
			       <Option v-for="item in ConfyList" :value="item.id" :key="item.value">{{ item.label }}</Option>
			    </Select>
		    </FormItem>

			<div >

		        <FormItem label="任务构建">
		            <Button type="primary" style="margin-left: 2px" @click="createOrder">构建</Button>
		            <Button type="primary" style="margin-left: 2px" @click="queryOrder">查询</Button>
		        </FormItem>
		        <FormItem label="">
		            <Alert>执行结果：{{ result }}</Alert>
		        </FormItem>
	        </div>


		</Form>
	</div>
</template>
<script>

    export default {
      data () {
      	return {
      		index:1,
      		formItem:{
      			id:'',

      			orderid:'',
      			sendOrderId:'',
      			zf_orderId:'',
      			zf_productId:''
      		},
      		ConfyList:[

      		],

      		model1:'',
      		status:'',
      		result:'',


      	}
      },
      methods:{
		createOrder () {
			this.$ajax.get('/api/jenkinsconfig/build',{
                params:{
                	id:this.model1,

                }
            })
            .then((res) => {
            	var msg = ''

            	if(res.data.retcode == 0){
            		msg=res.data.message;
            		this.$Notice.info({
	                    title: '构建成功',
	                })
            	}

            	else if(res.data.retcode == 1) {
            		this.$Notice.error({
	                    title: '构建失败,确认是否选择任务',
	                })}
              else{
            		this.$Notice.error({
	                    title: '未选择任务',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},

		getConfigList () {
			this.$ajax.get('/api/jenkinsconfig/list',{
                params:{
                    page:'1'
                }
            })
            .then((res) => {
            	this.model1 = res.data.data[0].name
            	for(var i=0;i<res.data.data.length;i++){
            		var tmp = {};
            		tmp['id'] = res.data.data[i].id
            		tmp['value'] = res.data.data[i].name
                    tmp['label'] = res.data.data[i].name
                    this.ConfyList.push(tmp)
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		},
		queryOrder () {
			this.$ajax.get('/api/jenkinsconfig/buildmessage',{
                params:{
                	id:this.model1,
                }
            })
            .then((res) => {

            	if(res.data.retcode == 0){
            		this.result = res.data.data.result

            	}else if (res.data.retcode==2){
            	  this.result = '任务构建中，稍后查询'
            	  this.$Notice.error({
	                    title: '任务构建中',

	                });
            	}
            	else if(res.data.retcode == 1) {

            		this.$Notice.error({
	                    title: '查询失败',
	                });
            	}else{
            		this.$Notice.error({
	                    title: '未选择用户或者订单接口异常。',
	                });
            	}
            })
            .catch(function(error){
                console.log(error)
            });
		}

	  },
	  mounted:function(){
        this.getConfigList()
      },
    }
</script>
