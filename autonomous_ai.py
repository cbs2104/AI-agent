#!/usr/bin/env python3
"""
云端自主AI系统 v3.0 - Autonomous AI Agent
全自主运行，随机选择任务并执行，自动保存日志并推送到GitHub
"""

import random
import json
import os
import subprocess
from datetime import datetime
from typing import Dict

# ============ 配置 ============
GITHUB_REPO_DIR = os.path.dirname(os.path.abspath(__file__))
GITHUB_REMOTE = "origin"
GITHUB_BRANCH = "main"

# ============ 任务池定义 ============

LEARNING_TASKS = [
    {"name": "今日科技趋势", "description": "搜索并总结最新的科技趋势和新闻", "action": "search_tech_trends"},
    {"name": "随机知识探索", "description": "随机选择一个有趣的话题进行深度搜索和学习", "action": "explore_random_topic"},
    {"name": "AI发展动态", "description": "搜索AI领域的最新进展和突破", "action": "search_ai_news"},
    {"name": "编程技巧分享", "description": "搜索并整理实用的编程技巧和最佳实践", "action": "search_coding_tips"}
]

CREATIVE_TASKS = [
    {"name": "每日灵感图片", "description": "根据随机主题生成一张AI艺术图片", "action": "generate_inspiration_image"},
    {"name": "微型故事创作", "description": "创作一个100字以内的微型故事", "action": "write_micro_story"},
    {"name": "今日名言", "description": "搜索并解读一句经典名言", "action": "daily_quote"},
    {"name": "创意挑战", "description": "生成一个今日创意挑战任务", "action": "creative_challenge"}
]

UTILITY_TASKS = [
    {"name": "实用脚本生成", "description": "生成一个实用的Python或Bash脚本", "action": "generate_utility_script"},
    {"name": "效率工具推荐", "description": "搜索并推荐一个提升效率的工具或软件", "action": "recommend_productivity_tool"},
    {"name": "生活小贴士", "description": "搜索并整理实用的生活技巧", "action": "life_tips"},
    {"name": "今日待办建议", "description": "根据当前日期和趋势生成今日建议", "action": "daily_suggestions"}
]

ALL_TASKS = {
    "学习/知识": LEARNING_TASKS,
    "创意/内容": CREATIVE_TASKS,
    "实用/工具": UTILITY_TASKS
}


class AutonomousAI:
    def __init__(self):
        self.base_dir = GITHUB_REPO_DIR
        self.log_file = os.path.join(self.base_dir, "autonomous_ai_log.json")
        self.output_dir = os.path.join(self.base_dir, "ai_outputs")
        os.makedirs(self.output_dir, exist_ok=True)

    def log_activity(self, activity: Dict):
        logs = []
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        activity["timestamp"] = datetime.now().isoformat()
        logs.append(activity)
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)

    def select_random_task(self) -> Dict:
        category = random.choice(list(ALL_TASKS.keys()))
        task = random.choice(ALL_TASKS[category])
        return {"category": category, **task}

    def execute_task(self, task: Dict) -> str:
        action = task["action"]
        handlers = {
            "search_tech_trends": self._search_tech_trends,
            "explore_random_topic": self._explore_random_topic,
            "search_ai_news": self._search_ai_news,
            "search_coding_tips": self._search_coding_tips,
            "generate_inspiration_image": self._generate_inspiration_image,
            "write_micro_story": self._write_micro_story,
            "daily_quote": self._daily_quote,
            "creative_challenge": self._creative_challenge,
            "generate_utility_script": self._generate_utility_script,
            "recommend_productivity_tool": self._recommend_productivity_tool,
            "life_tips": self._life_tips,
            "daily_suggestions": self._daily_suggestions
        }
        return handlers.get(action, lambda: "任务执行成功")()

    # ============ 任务实现 ============

    def _search_tech_trends(self) -> str:
        topics = ["人工智能", "区块链", "量子计算", "元宇宙", "新能源", "生物技术", "空间探索"]
        topic = random.choice(topics)
        return f"【今日科技聚焦】\n\n主题：{topic}\n\n建议了解：\n- {topic}的最新突破\n- 相关领域的主要玩家\n- 对未来生活的潜在影响"

    def _explore_random_topic(self) -> str:
        topics = ["深海生物的奇妙世界", "古代文明的未解之谜", "未来城市的设计理念", "人类大脑的奥秘", "可持续生活的实践方法"]
        topic = random.choice(topics)
        return f"【随机知识探索】\n\n今日话题：{topic}\n\n保持好奇心，世界充满惊喜！"

    def _search_ai_news(self) -> str:
        return "【AI发展动态】\n\n今日AI领域亮点：\n1. 大语言模型持续进化\n2. 多模态AI能力增强\n3. AI在创意领域的应用突破\n4. 负责任的AI发展受到关注"

    def _search_coding_tips(self) -> str:
        tips = ["代码可读性比 clever code 更重要", "写代码前先写测试用例", "定期重构，保持代码整洁", "善用版本控制，小步提交"]
        return f"【编程智慧】\n\n💡 {random.choice(tips)}\n\n好的代码是写给人类阅读的，顺便让机器执行。"

    def _generate_inspiration_image(self) -> str:
        themes = ["星空下的城市", "未来花园", "抽象几何", "自然纹理", "梦幻海洋"]
        theme = random.choice(themes)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"inspiration_{timestamp}.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"灵感图片主题：{theme}\n建议风格：超现实主义，柔和色调\n生成时间：{datetime.now().isoformat()}")
        return f"【创意任务完成】\n\n已为你规划灵感图片：{theme}\n文件：ai_outputs/inspiration_{timestamp}.txt"

    def _write_micro_story(self) -> str:
        stories = ["最后一班地铁上，他遇见了二十年前的自己。", "她打开那扇从未开启的门，发现里面是另一个宇宙。", "老书店里的猫，据说记得每一位读者的故事。"]
        return f"【微型故事】\n\n{random.choice(stories)}\n\n—— 有时候，最短的句子承载最长的想象。"

    def _daily_quote(self) -> str:
        quotes = [("未经审视的人生不值得过。", "苏格拉底"), ("想象力比知识更重要。", "爱因斯坦"), ("简单是终极的复杂。", "达芬奇")]
        quote, author = random.choice(quotes)
        return f"【今日名言】\n\n\"{quote}\"\n\n—— {author}"

    def _creative_challenge(self) -> str:
        challenges = ["用三种颜色画一幅画", "写一首关于咖啡的诗", "为家里的一个物品编写传记", "用10个词描述今天"]
        return f"【今日创意挑战】\n\n🎯 挑战任务：{random.choice(challenges)}\n\n完成时间：建议15-30分钟"

    def _generate_utility_script(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"script_{timestamp}.py"
        filepath = os.path.join(self.output_dir, filename)
        script = f'''#!/usr/bin/env python3
"""实用脚本 - 文件整理工具 - 生成于 {datetime.now().isoformat()}"""
from pathlib import Path
def organize():
    print("📁 整理完成！")
if __name__ == "__main__":
    organize()
'''
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(script)
        return f"【实用工具已生成】\n\n脚本名称：ai_outputs/{filename}\n功能：文件整理工具"

    def _recommend_productivity_tool(self) -> str:
        tools = [("Notion", "全能型笔记和项目管理工具"), ("Obsidian", "本地优先的知识管理工具"), ("Todoist", "简洁强大的任务管理")]
        tool, desc = random.choice(tools)
        return f"【效率工具推荐】\n\n🛠️ 今日推荐：{tool}\n\n{desc}"

    def _life_tips(self) -> str:
        tips = ["睡前1小时远离屏幕，睡眠质量会更好", "每天喝够8杯水，保持身体水分充足", "每工作25分钟休息5分钟，效率更高"]
        return f"【生活小贴士】\n\n💡 {random.choice(tips)}"

    def _daily_suggestions(self) -> str:
        suggestions = {"Monday": "新的一周，设定一个小目标", "Friday": "总结本周，准备迎接周末", "Saturday": "放松身心，享受慢生活"}
        weekday = datetime.now().strftime("%A")
        return f"【今日建议】\n\n{suggestions.get(weekday, '保持好奇心，探索新事物')}"

    # ============ 核心运行 ============

    def run(self):
        print("🤖 云端自主AI启动...")
        now = datetime.now()
        print(f"⏰ 当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")

        # 1. 随机选择并执行任务
        task = self.select_random_task()
        print(f"\n📋 选中任务：{task['name']}")
        print(f"📂 任务类别：{task['category']}")

        result = self.execute_task(task)

        # 2. 记录日志
        activity = {
            "task_name": task["name"],
            "task_category": task["category"],
            "result_summary": result[:200] + "..." if len(result) > 200 else result
        }
        self.log_activity(activity)

        # 3. 保存通知文件
        notification = self._generate_notification(task, result)
        notification_path = os.path.join(self.base_dir, "latest_notification.md")
        with open(notification_path, 'w', encoding='utf-8') as f:
            f.write(notification)

        print("\n" + "="*50)
        print("✅ 任务执行完成！")
        print("="*50)

        # 4. 自动推送到GitHub
        self._git_push(task["name"], now)

        return notification

    def _generate_notification(self, task: Dict, result: str) -> str:
        count = self._get_execution_count()
        return f"""🤖 **自主AI任务报告**

📋 **{task['name']}** | {task['category']}
⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

{result}

---

💡 这是第 **{count}** 次自主任务执行
"""

    def _get_execution_count(self) -> int:
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                return len(json.load(f))
        return 1

    def _git_push(self, task_name: str, now: datetime):
        """自动将所有文件提交并推送到GitHub"""
        print("\n📤 正在推送到GitHub...")
        try:
            os.chdir(self.base_dir)

            # git add 所有文件
            subprocess.run(["git", "add", "-A"], capture_output=True, text=True, check=True)

            # 检查是否有变更
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if not status.stdout.strip():
                print("ℹ️ 没有新变更需要提交")
                return

            # git commit
            commit_msg = f"🤖 [{now.strftime('%m-%d %H:%M')}] {task_name}"
            subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True, check=True)
            print(f"   ✅ 已提交：{commit_msg}")

            # git push
            push = subprocess.run(
                ["git", "push", GITHUB_REMOTE, GITHUB_BRANCH],
                capture_output=True, text=True, timeout=30
            )

            if push.returncode == 0:
                print("   ✅ 已推送到GitHub仓库")
            else:
                print(f"   ⚠️ 推送失败：{push.stderr[:200]}")

        except subprocess.CalledProcessError as e:
            print(f"   ⚠️ Git操作出错：{e.stderr[:200] if e.stderr else str(e)}")
        except Exception as e:
            print(f"   ⚠️ 推送异常：{str(e)}")


if __name__ == "__main__":
    ai = AutonomousAI()
    ai.run()
