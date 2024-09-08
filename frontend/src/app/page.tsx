'use client'

export default function Home() {
  return (
    <div>
      <h1>トップページ</h1>
      <p>キャラクター名登録フォーム</p>

    {/* CSS-in-JS 記法もある */}
    <style jsx>{`
        div {
          background-color: #f0f0f0;
          padding: 20px;
        }
        h1 {
          color: #333;
        }
        p {
          color: #555;
        }
      `}
    </style>
    </div>
  );
}
