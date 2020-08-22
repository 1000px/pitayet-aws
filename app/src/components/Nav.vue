<template>
  <v-navigation-drawer
    v-model="$store.state.navShown"
    fixed
    right
  >
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>John Leider</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <v-treeview
      activatable
      color="warning"
      :items="navs"
      @update:active="updateNav"
    >
    </v-treeview>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Nav',
  data () {
    return {
      navs: []
    }
  },
  mounted () {
    this.$server.get('subjects/').then(data => {
      this.navs = data
    })
  },
  methods: {
    updateNav (arr) {
      if (arr.length >= 1) {
        let id = arr[0]
        let crumbs = getNavById(this.navs, id, [])
        this.$store.dispatch('updateBreadcrumbsFun', crumbs)
      }
    }
  }
}
// 对Array进行循环遍历，对第一个元素进行判断，
//     如果id相等，则将当前元素push到result中，并返回。
//     如果id不相等，
//         首先将当前元素push到result数组中, 如果当前元素有子数组，则递归迭代
//         如果当前元素没有子数组，则result=[]
//     进入下一元素循环
function getNavById (arr, id, result = []) {
  if (!arr.length) return []
  let len = arr.length
  let i
  let isOver = false
  for (i = 0; i < len; i++) {
    let item = arr[i]
    // 定制新元素
    item.text = item.name
    item.href = item.url
    result.push(item)
    if (item.id === id) {
      item.href = ''
      isOver = true
      break
    } else {
      if (item.children && item.children.length >= 1) {
        result = getNavById(item.children, id, result)
        if (result.length) return result
      } else {
        result.pop()
      }
    }
  }
  if (!isOver) {
    result = []
  }
  return result
}
</script>

<style>

</style>
