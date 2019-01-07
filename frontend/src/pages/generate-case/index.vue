<style scoped>
	 @import './index.css';
</style>
<template>
	<div>
		<div class="case-zone">
			<Form :model="formItem" :label-width="110">
				<FormItem label="用例生成方式">
		            <Select v-model="formItem.defaultGen" placeholder="生成测试用例的方法">
				        <Option v-for="item in formItem.generateMethod" :value="item.value" :key="item.label">{{ item.label }}</Option>
				    </Select>
		        </FormItem>
		        <div v-if="formItem.seenGen1">
			        <FormItem label="接口对应域名">
			            <Select v-model="formItem.defaultDomain" placeholder="接口域名" @on-change="changeDomain()">
					        <Option v-for="item in formItem.domainName" :value="item.id" :key="item.value">{{ item.label }}</Option>
					    </Select>
			        </FormItem>
			        <FormItem label="生成用例归属项目" > 
			            <Select v-model="formItem.defaultPro" placeholder="新生成的用例归属项目">
					        <Option v-for="item in formItem.genProname" :value="item.value" :key="item.value">{{ item.label }}</Option>
					    </Select>
			        </FormItem>
			        <FormItem label="已有用例项目名称" >
			            <Select v-model="formItem.pname" placeholder="已有用例项目名称" @on-change="changeName">
					        <Option v-for="item in formItem.hadProname" :value="item.value" :key="item.value">{{ item.label }}</Option>
					    </Select>
			        </FormItem>
			        <FormItem label="用例名称">
			        	<CheckboxGroup v-model="social" @on-change="selectionCase()">
					    	<Checkbox v-for="item in formItem.caseName" :value="item.value" :key="item.id" :label="item.value">{{ item.label }}</Checkbox>
					    </CheckboxGroup>
			        </FormItem>
		        </div>
		        <FormItem>
		            <Button type="primary" style="margin-left: 8px" @click="generate()">生成</Button>
		        </FormItem>
		    </Form>
	    </div>
	</div>
</template>
<script>

	import uniq from 'lodash/uniq'
    export default {
    	data () {
		    return {
		        formItem: {
		        	defaultGen:'按已有用例生成',
		        	generateMethod: [
		        		{value: '按已有用例生成',label: '按已有用例生成'},
		        		{value: '按接口参数生成',label: '按接口参数生成'},
		        	],
		        	seenGen1:true,
		            genProname: [
		            ],
		            defaultPro:'',
		            hadProname: [
		            ],
		            defaultDomain:'',
		            domainName: [
		            ],
		            caseName:[
		            ],
		            conf:'',
		            pname:''
		        },
		        social: [],
		    }
		},
		methods: {
			getConfig () {
	        	this.$ajax.get('/api/ipconfig/listopt',{
	        		params:{
	        		}
	        	})
	    		.then((res) => {

	    			//项目
	    			for(var i=0;i<res.data.data.project.length;i++){
	    				var gpro = {};
	    				gpro['value'] = res.data.data.project[i];
	    				gpro['label'] = res.data.data.project[i];
	    				this.formItem.defaultPro = res.data.data.project[0];
	    				this.formItem.conf = res.data.data.project[0];
	    				this.formItem.genProname.push(gpro)
	    				this.formItem.hadProname.push(gpro)
	    			}

	                //域名
	                for(var j=0;j<res.data.data.ipconfig.length;j++){
	                	var tmpDomain = {};
	                	tmpDomain['id'] = res.data.data.ipconfig[j]._id;
	                	tmpDomain['value'] = res.data.data.ipconfig[j].url;
	                	tmpDomain['label'] = res.data.data.ipconfig[j].url;
	                	this.formItem.defaultDomain = res.data.data.ipconfig[0].url;
	                	this.formItem.domainName.push(tmpDomain);
	                }
	            })
	    		.catch(function(error){
	    			console.log(error)
	    		});
	        },
	        getCase () {
	        	this.$ajax.get('/api/ipconfig/listcase',{
	        		params:{
	        			proname:this.formItem.pname
	        		}
	        	})
	    		.then((res) => {
	    			console.log(res.data)
	            })
	    		.catch(function(error){
	    			console.log(error)
	    		});
	        },
	        changeName () {
	        	console.log(this.formItem.caseName)
	        	this.$ajax.get('/api/ipconfig/listcase',{
	        		params:{
	        			proname:this.formItem.pname
	        		}
	        	})
	    		.then((res) => {
	    			
	    			var tmp = []
	    			for(var i=0;i<res.data.data.case.length;i++){
	    				this.formItem.pname = res.data.data.case[0].name;
	    				var tmpCase = {};
	    				if(res.data.retcode == 0){
		    				tmpCase['id'] = res.data.data.case[i].id;
		    				tmpCase['value'] = res.data.data.case[i].name;
		    				tmpCase['label'] = res.data.data.case[i].name;
		    				tmp.push(tmpCase)	
	    				}
	    				this.formItem.caseName = tmp
	    			}
	            })
	    		.catch(function(error){
	    			console.log(error)
	    		});
	        },
	        changeDomain () {
	        	console.log(this.formItem.defaultDomain)
	        },
	        generate () {
	        	console.log(this.social)
	        	this.$ajax.get('/api/ipconfig/gencase',{
	        		params:{
	        			cid:this.social.join(','),
	        			configid:this.formItem.defaultDomain,
	        			proname:this.formItem.defaultPro,
	        		}
	        	})
	    		.then((res) => {
	    			if(res.data.retcode == 0) {
	    				this.$router.push('/case/list')
	    			}
	            })
	    		.catch(function(error){
	    			console.log(error)
	    		});
	        },
	        selectionCase () {
	        	uniq(this.social)
	        }
		},
		mounted:function(){
			this.getConfig()
	    },
    }
</script>