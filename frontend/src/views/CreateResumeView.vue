<template>
  <div class="create-resume-view">
    <div class="container">
      <n-space vertical size="large">
        <div class="page-header">
          <h1 class="page-title">创建您的专业简历</h1>
          <p class="page-description">填写您的信息，我们将帮助您生成专业的简历内容</p>
        </div>
        
        <n-card>
          <n-tabs type="line" animated>
            <n-tab-pane name="basics" tab="基本信息">
              <n-form
                ref="basicsFormRef"
                :model="resumeStore.resumeForm.basics"
                label-placement="left"
                label-width="auto"
                require-mark-placement="right-hanging"
              >
                <n-form-item label="姓名" path="name" :rule="{ required: true, message: '请输入您的姓名' }">
                  <n-input v-model:value="resumeStore.resumeForm.basics.name" placeholder="请输入您的姓名" />
                </n-form-item>
                
                <n-form-item label="职位/头衔" path="label">
                  <n-input v-model:value="resumeStore.resumeForm.basics.label" placeholder="如：前端开发工程师" />
                </n-form-item>
                
                <n-form-item label="电子邮箱" path="email" :rule="{ type: 'email', required: true, message: '请输入有效的电子邮箱' }">
                  <n-input v-model:value="resumeStore.resumeForm.basics.email" placeholder="请输入您的电子邮箱" />
                </n-form-item>
                
                <n-form-item label="联系电话" path="phone">
                  <n-input v-model:value="resumeStore.resumeForm.basics.phone" placeholder="请输入您的联系电话" />
                </n-form-item>
                
                <n-form-item label="所在地" path="location">
                  <n-input v-model:value="resumeStore.resumeForm.basics.location" placeholder="如：北京市朝阳区" />
                </n-form-item>
                
                <n-form-item label="个人概述" path="summary">
                  <n-input
                    v-model:value="resumeStore.resumeForm.basics.summary"
                    type="textarea"
                    placeholder="简要介绍自己，包括您的专业技能、工作经验和职业目标"
                    :autosize="{ minRows: 3, maxRows: 6 }"
                  />
                </n-form-item>
              </n-form>
            </n-tab-pane>
            
            <n-tab-pane name="work" tab="工作经历">
              <div class="section-actions mb-4">
                <n-button @click="handleAddWork" type="primary" secondary>
                  <template #icon>
                    <n-icon><add-icon /></n-icon>
                  </template>
                  添加工作经历
                </n-button>
              </div>
              
              <n-collapse>
                <n-collapse-item
                  v-for="(work, index) in resumeStore.resumeForm.work"
                  :key="index"
                  :title="work.company || '未命名公司'"
                  :name="index"
                >
                  <template #header-extra>
                    <n-button quaternary circle size="small" @click.stop="handleRemoveWork(index)">
                      <template #icon>
                        <n-icon><close-icon /></n-icon>
                      </template>
                    </n-button>
                  </template>
                  
                  <n-form
                    :model="work"
                    label-placement="left"
                    label-width="auto"
                    require-mark-placement="right-hanging"
                  >
                    <n-form-item label="公司名称" path="company" :rule="{ required: true, message: '请输入公司名称' }">
                      <n-input v-model:value="work.company" placeholder="请输入公司名称" />
                    </n-form-item>
                    
                    <n-form-item label="职位" path="position" :rule="{ required: true, message: '请输入职位名称' }">
                      <n-input v-model:value="work.position" placeholder="请输入您的职位" />
                    </n-form-item>
                    
                    <n-grid :cols="2" :x-gap="16">
                      <n-gi>
                        <n-form-item label="开始日期" path="startDate">
                          <n-date-picker v-model:value="work.startDate" type="date" format="yyyy-MM" value-format="yyyy-MM" />
                        </n-form-item>
                      </n-gi>
                      <n-gi>
                        <n-form-item label="结束日期" path="endDate">
                          <n-date-picker v-model:value="work.endDate" type="date" format="yyyy-MM" value-format="yyyy-MM" clearable />
                        </n-form-item>
                      </n-gi>
                    </n-grid>
                    
                    <n-form-item label="工作内容" path="summary">
                      <n-input
                        v-model:value="work.summary"
                        type="textarea"
                        placeholder="描述您的工作职责和成就"
                        :autosize="{ minRows: 3, maxRows: 6 }"
                      />
                    </n-form-item>
                  </n-form>
                </n-collapse-item>
              </n-collapse>
              
              <n-empty v-if="resumeStore.resumeForm.work.length === 0" description="尚未添加工作经历" />
            </n-tab-pane>
            
            <n-tab-pane name="education" tab="教育经历">
              <div class="section-actions mb-4">
                <n-button @click="handleAddEducation" type="primary" secondary>
                  <template #icon>
                    <n-icon><add-icon /></n-icon>
                  </template>
                  添加教育经历
                </n-button>
              </div>
              
              <n-collapse>
                <n-collapse-item
                  v-for="(education, index) in resumeStore.resumeForm.education"
                  :key="index"
                  :title="education.institution || '未命名教育机构'"
                  :name="index"
                >
                  <template #header-extra>
                    <n-button quaternary circle size="small" @click.stop="handleRemoveEducation(index)">
                      <template #icon>
                        <n-icon><close-icon /></n-icon>
                      </template>
                    </n-button>
                  </template>
                  
                  <n-form
                    :model="education"
                    label-placement="left"
                    label-width="auto"
                    require-mark-placement="right-hanging"
                  >
                    <n-form-item label="学校/机构名称" path="institution" :rule="{ required: true, message: '请输入学校或机构名称' }">
                      <n-input v-model:value="education.institution" placeholder="请输入学校或机构名称" />
                    </n-form-item>
                    
                    <n-form-item label="学位/专业" path="area" :rule="{ required: true, message: '请输入专业名称' }">
                      <n-input v-model:value="education.area" placeholder="请输入您的专业" />
                    </n-form-item>
                    
                    <n-form-item label="学历/学位" path="studyType">
                      <n-select v-model:value="education.studyType" :options="studyTypeOptions" placeholder="请选择学历" />
                    </n-form-item>
                    
                    <n-grid :cols="2" :x-gap="16">
                      <n-gi>
                        <n-form-item label="开始日期" path="startDate">
                          <n-date-picker v-model:value="education.startDate" type="date" format="yyyy-MM" value-format="yyyy-MM" />
                        </n-form-item>
                      </n-gi>
                      <n-gi>
                        <n-form-item label="结束日期" path="endDate">
                          <n-date-picker v-model:value="education.endDate" type="date" format="yyyy-MM" value-format="yyyy-MM" clearable />
                        </n-form-item>
                      </n-gi>
                    </n-grid>
                  </n-form>
                </n-collapse-item>
              </n-collapse>
              
              <n-empty v-if="resumeStore.resumeForm.education.length === 0" description="尚未添加教育经历" />
            </n-tab-pane>
            
            <n-tab-pane name="skills" tab="技能特长">
              <div class="section-actions mb-4">
                <n-button @click="handleAddSkill" type="primary" secondary>
                  <template #icon>
                    <n-icon><add-icon /></n-icon>
                  </template>
                  添加技能
                </n-button>
              </div>
              
              <n-collapse>
                <n-collapse-item
                  v-for="(skill, index) in resumeStore.resumeForm.skills"
                  :key="index"
                  :title="skill.name || '未命名技能'"
                  :name="index"
                >
                  <template #header-extra>
                    <n-button quaternary circle size="small" @click.stop="handleRemoveSkill(index)">
                      <template #icon>
                        <n-icon><close-icon /></n-icon>
                      </template>
                    </n-button>
                  </template>
                  
                  <n-form
                    :model="skill"
                    label-placement="left"
                    label-width="auto"
                    require-mark-placement="right-hanging"
                  >
                    <n-form-item label="技能名称" path="name" :rule="{ required: true, message: '请输入技能名称' }">
                      <n-input v-model:value="skill.name" placeholder="如：JavaScript" />
                    </n-form-item>
                    
                    <n-form-item label="技能等级" path="level">
                      <n-slider v-model:value="skill.level" :min="0" :max="5" :step="1" :tooltip="false" />
                      <div class="skill-level-text">{{ skillLevelText(skill.level) }}</div>
                    </n-form-item>
                    
                    <n-form-item label="关键词" path="keywords">
                      <n-dynamic-tags v-model:value="skill.keywords" />
                    </n-form-item>
                  </n-form>
                </n-collapse-item>
              </n-collapse>
              
              <n-empty v-if="resumeStore.resumeForm.skills.length === 0" description="尚未添加技能" />
            </n-tab-pane>
            
            <n-tab-pane name="projects" tab="项目经历">
              <div class="section-actions mb-4">
                <n-button @click="handleAddProject" type="primary" secondary>
                  <template #icon>
                    <n-icon><add-icon /></n-icon>
                  </template>
                  添加项目经历
                </n-button>
              </div>
              
              <n-collapse>
                <n-collapse-item
                  v-for="(project, index) in resumeStore.resumeForm.projects"
                  :key="index"
                  :title="project.name || '未命名项目'"
                  :name="index"
                >
                  <template #header-extra>
                    <n-button quaternary circle size="small" @click.stop="handleRemoveProject(index)">
                      <template #icon>
                        <n-icon><close-icon /></n-icon>
                      </template>
                    </n-button>
                  </template>
                  
                  <n-form
                    :model="project"
                    label-placement="left"
                    label-width="auto"
                    require-mark-placement="right-hanging"
                  >
                    <n-form-item label="项目名称" path="name" :rule="{ required: true, message: '请输入项目名称' }">
                      <n-input v-model:value="project.name" placeholder="请输入项目名称" />
                    </n-form-item>
                    
                    <n-form-item label="项目描述" path="description">
                      <n-input
                        v-model:value="project.description"
                        type="textarea"
                        placeholder="描述项目的主要功能和目标"
                        :autosize="{ minRows: 3, maxRows: 6 }"
                      />
                    </n-form-item>
                    
                    <n-grid :cols="2" :x-gap="16">
                      <n-gi>
                        <n-form-item label="开始日期" path="startDate">
                          <n-date-picker v-model:value="project.startDate" type="date" format="yyyy-MM" value-format="yyyy-MM" />
                        </n-form-item>
                      </n-gi>
                      <n-gi>
                        <n-form-item label="结束日期" path="endDate">
                          <n-date-picker v-model:value="project.endDate" type="date" format="yyyy-MM" value-format="yyyy-MM" clearable />
                        </n-form-item>
                      </n-gi>
                    </n-grid>
                    
                    <n-form-item label="我的职责" path="highlights">
                      <n-dynamic-input
                        v-model:value="project.highlights"
                        placeholder="添加您在项目中的职责或成就"
                        :min="0"
                        :max="10"
                      >
                        <template #create-button-default>
                          添加职责/成就
                        </template>
                        <template #default="{ value, index }">
                          <n-input v-model:value="project.highlights[index]" placeholder="描述您的职责或成就" />
                        </template>
                      </n-dynamic-input>
                    </n-form-item>
                  </n-form>
                </n-collapse-item>
              </n-collapse>
              
              <n-empty v-if="resumeStore.resumeForm.projects.length === 0" description="尚未添加项目经历" />
            </n-tab-pane>
          </n-tabs>
        </n-card>
        
        <n-card title="简历模板">
          <div class="templates-section">
            <div class="templates-grid">
              <div 
                v-for="template in templates" 
                :key="template.id"
                class="template-item"
                :class="{ 'active': resumeStore.selectedTemplate === template.id }"
                @click="resumeStore.selectTemplate(template.id)"
              >
                <div class="template-preview">
                  <img :src="template.preview" :alt="template.name" />
                </div>
                <div class="template-name">{{ template.name }}</div>
              </div>
            </div>
          </div>
        </n-card>
        
        <div class="form-actions">
          <n-space justify="center">
            <n-button @click="resetForm">
              重置表单
            </n-button>
            <n-button type="primary" size="large" @click="generateResume" :loading="resumeStore.generating">
              生成简历
            </n-button>
          </n-space>
        </div>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useResumeStore } from '@/store/resume'
import { useMessage } from 'naive-ui'
import {
  NSpace,
  NCard,
  NTabs,
  NTabPane,
  NForm,
  NFormItem,
  NInput,
  NButton,
  NCollapse,
  NCollapseItem,
  NDatePicker,
  NGrid,
  NGi,
  NEmpty,
  NSlider,
  NDynamicTags,
  NDynamicInput,
  NIcon,
  NSelect
} from 'naive-ui'
import {
  Add as AddIcon,
  Close as CloseIcon
} from '@vicons/ionicons5'

const resumeStore = useResumeStore()
const message = useMessage()
const router = useRouter()

// 表单引用
const basicsFormRef = ref(null)

// 学历选项
const studyTypeOptions = [
  { label: '博士', value: '博士' },
  { label: '硕士', value: '硕士' },
  { label: '本科', value: '本科' },
  { label: '专科', value: '专科' },
  { label: '高中', value: '高中' }
]

// 示例模板
const templates = [
  {
    id: 'modern',
    name: '现代简约',
    preview: 'https://via.placeholder.com/150x200?text=现代简约'
  },
  {
    id: 'professional',
    name: '专业商务',
    preview: 'https://via.placeholder.com/150x200?text=专业商务'
  },
  {
    id: 'creative',
    name: '创意设计',
    preview: 'https://via.placeholder.com/150x200?text=创意设计'
  },
  {
    id: 'minimal',
    name: '极简风格',
    preview: 'https://via.placeholder.com/150x200?text=极简风格'
  }
]

// 模拟加载模板
onMounted(() => {
  // 实际项目中应从API加载模板
  resumeStore.selectTemplate('modern')
})

// 技能等级文本
const skillLevelText = (level) => {
  const levels = ['不了解', '了解', '熟悉', '掌握', '精通', '专家']
  return levels[level] || '未设置'
}

// 添加工作经历
const handleAddWork = () => {
  resumeStore.resumeForm.work.push({
    company: '',
    position: '',
    startDate: null,
    endDate: null,
    summary: ''
  })
}

// 删除工作经历
const handleRemoveWork = (index) => {
  resumeStore.resumeForm.work.splice(index, 1)
}

// 添加教育经历
const handleAddEducation = () => {
  resumeStore.resumeForm.education.push({
    institution: '',
    area: '',
    studyType: '',
    startDate: null,
    endDate: null
  })
}

// 删除教育经历
const handleRemoveEducation = (index) => {
  resumeStore.resumeForm.education.splice(index, 1)
}

// 添加技能
const handleAddSkill = () => {
  resumeStore.resumeForm.skills.push({
    name: '',
    level: 3,
    keywords: []
  })
}

// 删除技能
const handleRemoveSkill = (index) => {
  resumeStore.resumeForm.skills.splice(index, 1)
}

// 添加项目经历
const handleAddProject = () => {
  resumeStore.resumeForm.projects.push({
    name: '',
    description: '',
    startDate: null,
    endDate: null,
    highlights: []
  })
}

// 删除项目经历
const handleRemoveProject = (index) => {
  resumeStore.resumeForm.projects.splice(index, 1)
}

// 重置表单
const resetForm = () => {
  resumeStore.resetResumeForm()
}

// 生成简历
const generateResume = async () => {
  try {
    if (!resumeStore.resumeForm.basics.name) {
      return message.error('请至少填写姓名等基本信息')
    }

    await resumeStore.createResume()
    message.success('简历创建成功')
    router.push('/preview')
  } catch (error) {
    message.error('创建简历失败：' + (error.message || '未知错误'))
  }
}
</script>

<style scoped>
.page-header {
  text-align: center;
  margin-bottom: 2rem;
}

.page-title {
  font-size: 2rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.page-description {
  font-size: 1.1rem;
  color: var(--text-secondary);
}

.section-actions {
  margin-bottom: 1rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.skill-level-text {
  text-align: center;
  margin-top: 0.5rem;
  color: var(--text-secondary);
}

.templates-section {
  padding: 1rem 0;
}

.templates-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1.5rem;
}

.template-item {
  border: 2px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.template-item:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
}

.template-item.active {
  border-color: var(--primary-color);
}

.template-preview {
  height: 200px;
  overflow: hidden;
}

.template-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.template-name {
  padding: 0.5rem;
  text-align: center;
  font-weight: 500;
}

.form-actions {
  margin-top: 2rem;
  margin-bottom: 2rem;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .templates-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style> 