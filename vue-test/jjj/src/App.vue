<template>
  <div id="app">
<el-container>
  <el-header>信息收集中心</el-header>
  <el-container>
    <el-aside width="200px">

 <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">

      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">导航一</span>
      </el-menu-item>

      <el-menu-item index="2">
        <i class="el-icon-setting"></i>
        <span slot="title">导航二</span>
      </el-menu-item>


    </el-menu>

</el-aside>
    <el-main></el-main>
  </el-container>
</el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.el-header, .el-footer {
    background-color: #232C42;
    color: #e2e2e2;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #324157;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

</style>
