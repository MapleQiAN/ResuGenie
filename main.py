import uvicorn
import os

if __name__ == "__main__":
    # 检查是否有环境变量设置端口
    port = int(os.getenv("PORT", "8000"))
    
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
