'use client'

import Input from '@mui/joy/Input';
import Button from '@mui/joy/Button';
import Add from '@mui/icons-material/Add';
import { useState } from 'react';
// import { useAddCharacter } from './hooks/useAddCharacter';
import { useGetCharacter } from './hooks/useGetCharacter';

// 環境変数行き予定
const API_URL = 'http://localhost:8000'

export default function Home() {

  // const { AddData, addError, addIsLoading } = useAddCharacter()
  const { getData, getError, getIsLoading } = useGetCharacter()

  // 名前フォーム初期値設定
  const [name, setName] = useState('')

  const setInputValue =  (value: string) => {
    console.log('入力されました', value);
    setName(value)
  }

  const addCharacter = async () => {
    console.log(name, 'キャラクターの追加');

    if (name) {
      const response = await fetch(`${API_URL}/regist/character`, {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name,
        }),
      })

      try {
        if (response.ok) {
          console.log(response);
          setName('');
        }
      } catch (error) {
        console.log(error);
      }
    } else {
      console.log("値を入れて");
    }
  }

  return (
    <div className='content'>
      <div className='input_container'>
        <p>キャラクター名登録フォーム</p>
        <Input
          value={name}
          onChange={(event) => setInputValue(event.target.value)}
          placeholder='キャラクター名'
          color="neutral"
          size="md"
          variant="outlined"
        />
        <Button
          variant="solid"
          startDecorator={<Add />}
          onClick={addCharacter}
        >
          追加
        </Button>
      </div>
        

    {/* CSS-in-JS 記法もある */}
    <style jsx>{`
        .content {
          display: flex;
          justify-content: center;
          padding-top: 300px;
        }
        p {
          color: #555;
        }
        .input_container {
          display: flex;
          flex-direction: column;
          gap: 20px;
          padding: 20px;
          background-color: #f0f0f0;
          max-width: 300px;
        }
      `}
    </style>
    </div>
  );
}
