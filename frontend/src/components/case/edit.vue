<style scoped>
  @import './edit.css';
</style>
<template>
  <div>
    <div class="case-zone">
      <Form :model="formItem" :label-width="80">
        <FormItem label="测试集名称">
          <Input v-model="formItem.testsuits" placeholder="输入测试集名称"></Input>
        </FormItem>
        <FormItem label="所属项目">
          <Select v-model="formItem.project" placeholder="请选择接口所属项目">
            <Option v-for="item in formItem.proname" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </FormItem>
        <FormItem label="接口级别">
          <Select v-model="formItem.apiLevel" placeholder="请选择接口级别">
            <Option v-for="item in formItem.level" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </FormItem>
        <FormItem label="通用配置" >
          <Select v-model="formItem.conf" placeholder="请选择接口通用配置">
            <Option v-for="item in formItem.config" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </FormItem>
        <Form :label-width="80" ref="formComsDynamic" :model="formComsDynamic">
          <div
            v-for="(item,index) in formComsDynamic.items"
            v-if="item.status"
            :key="index"
            :prop="'items.' + index + '.value'">
            <FormItem label="">
              <Input v-model="formComsDynamic.items[index].url">
              <Select v-model="formComsDynamic.items[index].method" slot="prepend" style="width: 80px">
                <Option value="GET">GET</Option>
                <Option value="POST">POST</Option>
              </Select>
              <Button slot="append" type="primary" @click="send(index)">Send</Button>
              </Input>
            </FormItem>
            <Request ref="Request"></Request>
            <FormItem>
              <Button type="error" @click="handleRemove(index)" size="small">删除接口</Button>
            </FormItem>
          </div>
        </Form>
        <FormItem label="接口响应" v-if="seen">
          <Input v-model="formItem.textarea" type="textarea" :autosize="{minRows: 2,maxRows: 15}"></Input>
        </FormItem>
        <FormItem>
          <Button type="success"  @click="handleAdd">新增接口</Button>
          <Button type="primary" style="margin-left: 8px" @click="update()">更新</Button>
          <Button type="warning" style="margin-left: 8px" @click.native="$router.push('/case/list')">取消</Button>
        </FormItem>
      </Form>
    </div>
  </div>
</template>
<script>

import Header from '../header/header.vue'
import Request from './request.vue'
export default {

  components: { Header, Request },
  data () {
    return {
      formItem: {
        testsuits: '',
        proname: [
          // {value: 'New York',label: 'New York'}
        ],
        level: [
          {value: '1', label: '1'},
          {value: '2', label: '2'},
          {value: '3', label: '3'}
        ],
        config: [
          // {value: 'New York',label: 'New York'}
        ],
        ding: '',
        pdata: '',
        slider: [20, 50],
        // textarea: JSON.stringify({ "product": "1", "device-id": "867600024493404", "Content-Length": "47", "appver": "5.8.9", "app_ver": "5.8.9", "platform-type": "1", "upk": "911877d3c2dd49a8b05ba73d79003511%7C462806171677%7C9d4c96d348b34ff0b5a449800423b977%7C60F6528F2F9ED7EEC0A850582C289827", "platform-ver": "6.0", "sysver": "6.0", "device_id": "867600024493404", "app-ver": "5.8.9" }, null, 4),
        value13: 'http://www.secoo.com',
        skip: '跳过',
        project: '',
        apiLevel: '1',
        conf: '',
        textarea: ''
      },
      index: 1,
      formComsDynamic: {
        items: [
          {
            value: '',
            index: 1,
            status: 1,
            key: '',
            url: '',
            method: 'GET'
          }
        ]
      },
      seen: false

    }
  },
  methods: {
    handleAdd () {
      this.index++
      this.formComsDynamic.items.push({
        value: '',
        index: this.index,
        status: 1,
        key: '',
        url: '',
        method: 'GET'
      })
    },
    handleRemove (index) {
      this.formComsDynamic.items[index].status = 0
      this.formComsDynamic.items.splice(index, 1)
    },
    update () {
      var reqdata1 = {}
      var reqdata2 = {}
      var dl = []

      var dataList = this.$refs.Request
      for (var i = 0; i < dataList.length; i++) {
        dl.push(dataList[i]._data)
      }

      reqdata1['data1'] = dl
      reqdata2['data2'] = this.formComsDynamic.items

      this.$ajax.get('/api/case/update', {
        params: {
          id: localStorage.getItem('case_id'),
          testsuitname: this.formItem.testsuits,
          proname: this.formItem.project,
          level: this.formItem.apiLevel,
          conf: this.formItem.conf,
          reqdata1: reqdata1,
          reqdata2: reqdata2
        }
      })
        .then((res) => {
          if (res.data.retcode === 0) {
            this.$router.push('/case/list')
          } else {
            this.$Notice.error({
              title: '更新失败'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    send (index) {
      var reqdata1 = {}
      var reqdata2 = {}
      var dl = []

      var dataList = this.$refs.Request
      for (var i = 0; i < dataList.length; i++) {
        dl.push(dataList[i]._data)
      }

      reqdata1['data1'] = dl[index]
      reqdata2['data2'] = this.formComsDynamic.items[index]

      // console.log(index)
      // console.log(this.formComsDynamic.items)
      // console.log(dl)
      this.$ajax.get('/api/case/runtest', {
        params: {
          testsuitname: this.formItem.testsuits,
          proname: this.formItem.project,
          level: this.formItem.apiLevel,
          conf: this.formItem.conf,
          reqdata1: reqdata1,
          reqdata2: reqdata2
        }
      })
        .then((res) => {
          // console.log(res.data)
          if (res.data.retcode === 0) {
            this.seen = true
            this.formItem.textarea = JSON.stringify(res.data.message.response, null, 4)
          } else if (res.data.retcode === 1) {
            this.$Notice.error({
              title: '引用变量解析失败'
            })
          } else {
            this.$Notice.error({
              title: '测试失败'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    handleReset (name) {
      this.$refs[name].resetFields()
    },
    handleSubmit (name) {
      console.log(this.formParamsDynamic)
    },
    getProName () {
      this.$ajax.get('/api/project/list', {
        params: {
        }
      })
        .then((res) => {
          for (var i = 0; i < res.data.data.length; i++) {
            var tmppd = {}
            // console.log(res.data.data[i].pro_name)
            tmppd['value'] = res.data.data[i].pro_name
            tmppd['label'] = res.data.data[i].pro_name

            this.formItem.proname.push(tmppd)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getConfName () {
      this.$ajax.get('/api/conf/list', {
        params: {
        }
      })
        .then((res) => {
          for (var i = 0; i < res.data.result.length; i++) {
            var tmppd = {}
            tmppd['value'] = res.data.result[i].name
            tmppd['label'] = res.data.result[i].name

            this.formItem.config.push(tmppd)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  created: function () {
    console.log('created')
    var cid = localStorage.getItem('case_id')
    this.$ajax.get('/api/case/listid', {
      params: {
        id: cid
      }
    })
      .then((res) => {
        if (res.data.retcode === 0) {
          // console.log(res)
          this.formItem.testsuits = res.data.data.testsuitname
          this.formItem.project = res.data.data.proname
          this.formItem.apiLevel = res.data.data.level
          this.formItem.conf = res.data.data.conf
          this.formComsDynamic.items = res.data.data.reqdata.reqdata2.data2
        } else {
          this.$Notice.error({
            title: '查询失败'
          })
        }
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  updated: function () {
    // console.log("updated")
  },
  mounted: function () {
    console.log('mounted')

    var cid = localStorage.getItem('case_id')
    this.$ajax.get('/api/case/listid', {
      params: {
        id: cid
      }
    })
      .then((res) => {
        if (res.data.retcode === 0) {
          // console.log(this.$refs.Request)
          for (var i = 0; i < res.data.data.reqdata.reqdata1.data1.length; i++) {
            this.$refs.Request[i]._data.formItem.name = res.data.data.reqdata.reqdata1.data1[i].formItem.name
            this.$refs.Request[i]._data.formItem.skip = res.data.data.reqdata.reqdata1.data1[i].formItem.skip
            this.$refs.Request[i]._data.formParamsDynamic = res.data.data.reqdata.reqdata1.data1[i].formParamsDynamic
            this.$refs.Request[i]._data.formHeadersDynmic = res.data.data.reqdata.reqdata1.data1[i].formHeadersDynmic
            this.$refs.Request[i]._data.formVariablesDynmic = res.data.data.reqdata.reqdata1.data1[i].formVariablesDynmic
            this.$refs.Request[i]._data.formExtractDynmic = res.data.data.reqdata.reqdata1.data1[i].formExtractDynmic
            this.$refs.Request[i]._data.formValidatorsDynmic = res.data.data.reqdata.reqdata1.data1[i].formValidatorsDynmic
          }
        } else {
          this.$Notice.error({
            title: '查询失败'
          })
        }
      })
      .catch(function (error) {
        console.log(error)
      })

    this.getProName()
    this.getConfName()
  },
  destroyed: function () {
    console.log('destroyed')
  }
}

</script>
