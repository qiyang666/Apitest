<style scoped>
  @import './request.css';
</style>
<template>
  <div class="">
        <FormItem label="">
            <Tabs value="name1" size="small" :animated="false">
              <TabPane label="CaseName" name="casename">
                <Input v-model="formItem.name" placeholder="输入测试用例名称"></Input>
              </TabPane>
              <TabPane label="Params" name="params">
                <Form ref="formParamsDynamic" :model="formParamsDynamic" :label-width="80">
                  <FormItem v-for="(item,index) in formParamsDynamic.items" v-if="item.status" :key="index" :prop="'items.' + index + '.value'">
                    <Row class="params-bottom">
                      <Col span="11" >
                        <Input type="text" v-model="formParamsDynamic.items[index].key" placeholder="Key"></Input>
                      </Col>
                      <Col span="11" class="params-width">
                        <Input type="text" placeholder="Value" v-model="formParamsDynamic.items[index].value"></Input>
                      </Col>
                      <Col span="1">
                        <Button type="error" @click="handleRemoveParams(index)">删除</Button>
                      </Col>
                    </Row>
                  </FormItem>
                  <FormItem style="width: 300px">
                    <Row>
                      <Col span="12">
                        <Button type="dashed" long @click="handleAddParams" icon="plus-round" size="small">Add item</Button>
                      </Col>
                    </Row>
                  </FormItem>
                </Form>
              </TabPane>
              <TabPane label="Headers" name="headers">
                <Form ref="formHeadersDynmic" :model="formHeadersDynmic" :label-width="80">
                  <FormItem v-for="(item,index) in formHeadersDynmic.items" v-if="item.status" :key="index" :prop="'items.' + index + '.value'">
                    <Row class="params-bottom">
                      <Col span="11" >
                        <Input type="text" v-model="formHeadersDynmic.items[index].key" placeholder="Key"></Input>
                      </Col>
                      <Col span="11" class="params-width">
                        <Input type="text" placeholder="Value" v-model="formHeadersDynmic.items[index].value"></Input>
                      </Col>
                      <Col span="1">
                        <Button type="error" @click="handleRemoveHeaders(index)">删除</Button>
                      </Col></Row>
                  </FormItem>
                  <FormItem style="width: 300px">
                    <Row>
                      <Col span="12">
                        <Button type="dashed" long @click="handleAddHeaders" icon="plus-round" size="small">Add item</Button>
                      </Col>
                    </Row>
                  </FormItem>
                </Form>
              </TabPane>
              <TabPane label="Variables" name="variables">
                <Form ref="formVariablesDynmic" :model="formVariablesDynmic" :label-width="80">
                  <FormItem v-for="(item,index) in formVariablesDynmic.items" v-if="item.status" :key="index" :prop="'items.' + index + '.value'">
                    <Row class="params-bottom">
                      <Col span="11" >
                        <Input type="text" v-model="formVariablesDynmic.items[index].key" placeholder="Key"></Input>
                      </Col>
                      <Col span="11" class="params-width">
                        <Input type="text" placeholder="Value" v-model="formVariablesDynmic.items[index].value"></Input>
                      </Col>
                      <Col span="1">
                        <Button type="error" @click="handleRemoveVariables(index)">删除</Button>
                      </Col>
                    </Row>
                  </FormItem>
                  <FormItem style="width: 300px">
                    <Row>
                      <Col span="12">
                        <Button type="dashed" long @click="handleAddVariables" icon="plus-round" size="small">Add item</Button>
                      </Col>
                    </Row>
                  </FormItem>
                </Form>
              </TabPane>
              <TabPane label="Extract" name="extract">
                <Form ref="formExtractDynmic" :model="formExtractDynmic" :label-width="80">
                  <FormItem v-for="(item,index) in formExtractDynmic.items" v-if="item.status" :key="index" :prop="'items.' + index + '.value'">
                    <Row class="params-bottom">
                      <Col span="11" >
                        <Input type="text" v-model="formExtractDynmic.items[index].key" placeholder="Key"></Input>
                      </Col>
                      <Col span="11" class="params-width">
                        <Input type="text" placeholder="Value" v-model="formExtractDynmic.items[index].value"></Input>
                      </Col>
                      <Col span="1">
                        <Button type="error" @click="handleRemoveExtract(index)">删除</Button>
                      </Col>
                    </Row>
                  </FormItem>
                  <FormItem style="width: 300px">
                    <Row>
                      <Col span="12">
                        <Button type="dashed" long @click="handleAddExtract" icon="plus-round" size="small">Add item</Button>
                      </Col>
                    </Row>
                  </FormItem>
                </Form>
              </TabPane>
              <TabPane label="Validators" name="validators">
                <Form ref="formValidatorsDynmic" :model="formValidatorsDynmic" :label-width="80" class="from-bottom">
                  <FormItem v-for="(item,index) in formValidatorsDynmic.items" v-if="item.status" :key="index" :prop="'items.' + index + '.value'">
                    <Row class="params-bottom">
                      <Col span="7" class="params-width">
                        <Input type="text" v-model="formValidatorsDynmic.items[index].check" placeholder="Check"></Input>
                      </Col>
                      <Col span="7" class="params-width">
                        <Select v-model="formValidatorsDynmic.items[index].comparator" placeholder="Select Comparator">
                          <Option v-for="item in formItem.comparator" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                      </Col>
                      <Col span="7" class="params-width">
                        <Input type="text" placeholder="Expected" v-model="formValidatorsDynmic.items[index].expected"></Input>
                      </Col>
                      <Col span="2">
                        <Button type="error" @click="handleRemoveValidators(index)">删除</Button>
                      </Col>
                    </Row>
                  </FormItem>
                  <FormItem style="width: 300px">
                    <Row>
                      <Col span="12">
                        <Button type="dashed" long @click="handleAddValidators" icon="plus-round" size="small">Add item</Button>
                      </Col>
                    </Row>
                  </FormItem>
                </Form>
              </TabPane>
              <TabPane label="Skip" name="skip">
                <RadioGroup v-model="formItem.skip">
                  <Radio label="跳过"></Radio>
                  <Radio label="不跳过"></Radio>
                </RadioGroup>
              </TabPane>
            </Tabs>
        </FormItem>
  </div>
</template>
<script>

export default {
  data () {
    return {
      formItem: {
        comparator: [
          {value: 'eq', label: 'eq'},
          {value: 'lt', label: 'lt'},
          {value: 'le', label: 'le'},
          {value: 'gt', label: 'gt'},
          {value: 'ge', label: 'ge'},
          {value: 'ne', label: 'ne'},
          {value: 'str_eq', label: 'str_eq'},
          {value: 'len_eq', label: 'len_eq'},
          {value: 'len_gt', label: 'len_gt'},
          {value: 'len_ge', label: 'len_ge'},
          {value: 'len_lt', label: 'len_lt'},
          {value: 'len_le', label: 'len_le'},
          {value: 'contains', label: 'contains'},
          {value: 'contained_by', label: 'contained_by'},
          {value: 'type_match', label: 'type_match'},
          {value: 'regex_match', label: 'regex_match'},
          {value: 'startswith', label: 'startswith'},
          {value: 'endswith', label: 'endswith'}
        ],
        method: 'GET',
        slider: [20, 50],
        textarea: '',
        value13: 'http://www.secoo.com',
        name: '',
        skip: '不跳过',
        md5: '',
        sign_md5: ''
      },
      index: 1,
      formParamsDynamic: {
        items: [
          {
            value: '',
            index: 1,
            status: 1,
            key: ''
          }
        ]
      },
      formHeadersDynmic: {
        items: [
          {
            value: '',
            index: 1,
            status: 1,
            key: ''
          }
        ]
      },
      formVariablesDynmic: {
        items: [
          {
            value: '',
            index: 1,
            status: 1,
            key: ''
          }
        ]
      },
      formExtractDynmic: {
        items: [
          {
            value: '',
            index: 1,
            status: 1,
            key: ''
          }
        ]
      },
      formValidatorsDynmic: {
        items: [
          {
            expected: 200,
            index: 1,
            status: 1,
            check: 'status_code',
            comparator: 'eq'
          }
        ]
      }
    }
  },
  methods: {
    handleAddParams () {
      this.index++
      this.formParamsDynamic.items.push({
        value: '',
        index: this.index,
        status: 1,
        key: ''
      })
    },
    handleRemoveParams (index) {
      this.formParamsDynamic.items[index].status = 0
      this.formParamsDynamic.items.splice(index, 1)
    },
    handleAddHeaders () {
      this.index++
      this.formHeadersDynmic.items.push({
        value: '',
        index: this.index,
        status: 1,
        key: ''
      })
    },
    handleRemoveHeaders (index) {
      this.formHeadersDynmic.items[index].status = 0
      this.formHeadersDynmic.items.splice(index, 1)
    },
    handleAddVariables () {
      this.index++
      this.formVariablesDynmic.items.push({
        value: '',
        index: this.index,
        status: 1,
        key: ''
      })
    },
    handleRemoveVariables (index) {
      this.formVariablesDynmic.items[index].status = 0
      this.formVariablesDynmic.items.splice(index, 1)
    },
    handleAddExtract () {
      this.index++
      this.formExtractDynmic.items.push({
        value: '',
        index: this.index,
        status: 1,
        key: ''
      })
    },
    handleRemoveExtract (index) {
      this.formExtractDynmic.items[index].status = 0
      this.formExtractDynmic.items.splice(index, 1)
    },
    handleAddValidators () {
      this.index++
      this.formValidatorsDynmic.items.push({
        value: '',
        index: this.index,
        status: 1,
        check: '',
        comparator: ''
      })
    },
    handleRemoveValidators (index) {
      this.formValidatorsDynmic.items[index].status = 0
      this.formValidatorsDynmic.items.splice(index, 1)
    },
    handleReset (name) {
      this.$refs[name].resetFields()
    },
    handleSubmit (name) {
      console.log(this.formParamsDynamic)
      console.log(this.formHeadersDynmic)
      console.log(this.formVariablesDynmic)
      console.log(this.formExtractDynmic)
      console.log(this.formValidatorsDynmic)
      // this.$refs[name].validate((valid) => {
      //     if (valid) {
      //         this.$Message.success('Success!');
      //     } else {
      //         this.$Message.error('Fail!');
      //     }
      // })
    },
    getMd5 () {
      console.log(this.formItem.md5)
      console.log(this.formParamsDynamic)
      this.$ajax.get('/api/case/sign', {
        params: {
          secret: this.formItem.md5,
          reqdata1: this.formParamsDynamic
        }
      })
        .then((res) => {
          if (res.data.success === 0) {
            this.formItem.sign_md5 = res.data.md5
            console.log(res.data.md5)
          } else {
            alert(res.data.message)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  mounted: function () {

  }
}
</script>
