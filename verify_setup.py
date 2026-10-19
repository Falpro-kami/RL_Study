import gymnasium as gym
import numpy as np

print(f"Gymnasium版本：{gym.__version__}")
print(f"NumPy版本：{np.__version__}")

try:
    # 创建一个简单环境
    env = gym.make("CartPole-v1", render_mode="rgb_array") # 如果需要图形输出，请使用“human”
    print("成功创建CartPole-v1环境。")

    # 重置环境以获得初始观测
    observation, info = env.reset(seed=42) # 使用种子以保证可重复性
    print(f"初始观测：{observation}")

    # 执行一个随机动作
    action = env.action_space.sample() # 采样一个随机动作（0或1）
    print(f"正在执行随机动作：{action}")

    # 执行动作
    observation, reward, terminated, truncated, info = env.step(action)

    print(f"下一观测：{observation}")
    print(f"获得的奖励：{reward}")
    print(f"回合结束：{terminated}")
    print(f"回合截断：{truncated}") # 截断表示达到时间限制

    # 关闭环境（清理很重要）
    env.close()
    print("环境互动成功。")

except Exception as e:
    print(f"验证过程中发生错误：{e}")
