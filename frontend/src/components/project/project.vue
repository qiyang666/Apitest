<style scoped>
  @import './project.css';
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
  <Input v-model="formItem.devploper" placeholder="输入开发人员名字"></Input>
  </FormItem>
  <FormItem label="报警邮箱">
  <Input v-model="formItem.mail" placeholder="输入接收报警邮箱地址"></Input>
  </FormItem>
  <FormItem label="钉钉地址">
  <Input v-model="formItem.ding" placeholder="输入钉钉机器人地址"></Input>
  </FormItem>
  <FormItem label="项目描述">
  <Input v-model="formItem.detail" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="项目简要描述"></Input>
  </FormItem>
  <FormItem>
  <Button type="primary" @click="save">保存</Button>
  <Button type="error" style="margin-left: 8px" @click.native="$router.push('/project/list')">取消</Button>
  </FormItem>
  </Form>
    </div>
</template>
<script>
// import Header from '../header/header.vue'
// import router from './router'
export default {
  data () {
    return {
      formItem: {
        proname: '',
        tester: '',
        devploper: '',
        detail: '',
        mail: '',
        ding: '',
        pdata: '',
        slider: [20, 50],
        textarea: ''
      },
      pdata: ''
    }
  },
  methods: {
    save () {
      var self = this
      this.$ajax.get('/api/project/create', {
        params: {
          pro_name: this.formItem.proname,
          tester: this.formItem.tester,
          developer: this.formItem.devploper,
          receive_mail: this.formItem.mail,
          dingding: this.formItem.ding,
          pro_detail: this.formItem.detail
        }
      })
        .then((res) => {
          this.pdata = res.data.retcode
          if (res.data.retcode === 0) {
            self.$router.push('/project/list')
          } else {
            this.$Notice.error({
              title: '添加失败'
            })
          }
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
