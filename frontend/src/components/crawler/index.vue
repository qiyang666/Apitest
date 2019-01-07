<style scoped>

</style>
<template>
  <div style="margin-left:auto;margin-right:auto;min-height: 200px;padding: 10px 50px;">
    <Row>
      <Col span="16">
         <Form :model="formItem" :label-width="100">
            <FormItem label="活动地址">
                <Input v-model="formItem.input" placeholder="Enter something..." style="max-width:700px;"></Input>
                <Button type="primary" @click="crawler">检查404专题</Button>
            </FormItem>
            <FormItem label="404专题ID">
                <div style="max-width:700px;">
                  <a v-for="url in formItem.urls" :href="url.content" target="showHere" @click="showIframe">{{ url.id }}</a>
                </div>
            </FormItem>
          </Form>
      </Col>
    <Col span="8" style="margin-top:50px;">
      <!-- <div class="accept-container">
            <div class="go-back" v-show="formItem.goBackState" @click="goBack">GoBack</div>
      </div> -->
      <iframe v-show="formItem.iframeState" id="show-iframe"  frameborder=0 name="showHere" scrolling=auto src=""></iframe>
    </Col>
    </Row>
  </div>
</template>
<script>

import $ from 'jquery'
export default {

  data () {
    return {
      formItem: {
        input: '',
        urls: [
          // {"id":"2345","content":"static/2345.html"},
          // {"id":"2346","content":"static/2345.html"},
          // {"id":"2347","content":"static/2345.html"},
          // {"id":"2348","content":"https://segmentfault.com/a/1190000004502619"},
          // {"id":"2349","content":"http://vuex.vuejs.org/"},
          // {"id":"24919","content":"https://las.secoo.com/api/topic/topic_list_new?id=24919&pageid=topicNew/24919"},
        ],
        iframeState: true,
        goBackState: false
      }
    }
  },
  methods: {
    crawler: function () {
      this.$store.dispatch('crawler/FETCH')
      // this.$store.dispatch('hello/REMOVE')
      console.log(this.$store)
      console.log(this.$store.state.crawler.list)
      console.log('hello')
      this.$Message.success({
        content: '已经开始测试,测试需要一段时间，你可以过一会儿回来，刷新页面查看最近一次测试结果',
        duration: 5
      })

      this.$ajax.get('/api/page404/test', {
        params: {
          url: this.formItem.input
        }
      })
        .then((res) => {
          console.log(res)
          if (res.data.retcode === 0) {
            console.log(res)
          } else {
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    goBack () {
      this.goBackState = false
      this.iframeState = false
    },
    showIframe () {
      this.goBackState = true
      this.iframeState = true
    }
  },
  mounted () {
    const oIframe = document.getElementById('show-iframe')
    const deviceWidth = document.documentElement.clientWidth
    const deviceHeight = document.documentElement.clientHeight
    oIframe.style.width = 320 + 'px'
    oIframe.style.height = 568 + 'px'
    // oIframe.style.background = "red";
    oIframe.style.border = 'solid 3px gray'
    // oIframe.style = {"box-shadow":"10px 10px 5px #888888"};
    // oIframe.style.box\-shadow = "10px 10px 5px #888888";
    this.$ajax.get('/api/page404/list', {
      params: {
      }
    })
      .then((res) => {
        console.log(res.data.data.result)
        var tmp = {}
        for (var i = 0; i < res.data.data.result.length; i++) {
          tmp['id'] = res.data.data.result[i].url
          tmp['content'] = 'static/' + res.data.data.result[i].error
        }

        this.formItem.urls.push(tmp)
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>
