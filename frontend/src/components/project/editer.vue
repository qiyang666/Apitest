<style scoped>
 @import './editer.css';
</style>
<template>
  <div class="pro-zone">
    <Form :model="formItem" :label-width="80">
      <FormItem label="项目名称">
        <Input v-model="formItem.proname" placeholder="输入项目名称"></Input>
  </FormItem>
  <FormItem label="测试人员">
    <Input v-model="formItem.tester" placeholder="输入测试人员名字"></Input>
  </FormItem>
  <FormItem label="开发人员">
  <Input v-model="formItem.developer" placeholder="输入开发人员名字"></Input>
  </FormItem>
  <FormItem label="报警邮箱">
  <Input v-model="formItem.mail" placeholder="输入接收报警邮箱地址"></Input>
  </FormItem>
  <!--<FormItem label="钉钉地址">-->
  <!--<Input v-model="formItem.ding" placeholder="输入钉钉机器人地址"></Input>-->
  <!--</FormItem>-->
  <FormItem label="项目描述">
  <Input v-model="formItem.detail" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="项目简要描述"></Input>
  </FormItem>
  <FormItem>
  <Button type="primary" @click="update()">更新</Button>
  <Button type="warning" style="margin-left: 8px" @click.native="$router.push('/project/list')">取消</Button>
  </FormItem>
  </Form>
  </div>
</template>
<script>
// import Header from '../header/header.vue'
export default {
  data () {
    return {
      formItem: {
        pid: localStorage.getItem('pid'),
        proname: localStorage.getItem('pro_name'),
        tester: localStorage.getItem('tester'),
        developer: localStorage.getItem('developer'),
        mail: localStorage.getItem('receive_mail'),
        ding: localStorage.getItem('dingding'),
        detail: localStorage.getItem('pro_detail'),
        time: '',
        slider: [20, 50],
        textarea: ''
      }
    }
  },
  methods: {
    update: function () {
      var self = this
      this.$ajax.get('/api/project/update', {
        params: {
          id: this.formItem.pid,
          pro_name: this.formItem.proname,
          tester: this.formItem.tester,
          developer: this.formItem.developer,
          receive_mail: this.formItem.mail,
          dingding: this.formItem.ding,
          pro_detail: this.formItem.detail
        }
      })
        .then((res) => {
          if (res.data.retcode === 0) {
            self.$router.push('/project/list')
          } else {
            this.$Notice.error({
              title: '更新失败'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
