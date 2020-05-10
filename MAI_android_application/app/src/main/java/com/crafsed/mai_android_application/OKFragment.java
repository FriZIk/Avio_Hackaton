package com.crafsed.mai_android_application;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.fragment.app.Fragment;

public class OKFragment extends Fragment {
    TextView mTextView;
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_ok, container, false);
        ActionBar actionBar = ((MainActivity)getActivity()).getSupportActionBar();
        actionBar.setTitle(getString(R.string.app_name)+" - Настройки");
        actionBar.setHomeButtonEnabled(true);
        actionBar.setDisplayHomeAsUpEnabled(true);
        mTextView = v.findViewById(R.id.textView5);
//        mTextView.setText(Port.text);
        mTextView.setText("Тип: Объект недвижимости\n" +
                "Вид: Земельный участок\n" +
                "Кадастровый номер: 50:07:00*****:52\n" +
                "Статус:" +
                "Учтенный\n" +
                "Адрес:\n" +
                "Категория: Земли сельскохозяйственного назначения\n" +
                "Кадастровая стоймость: 431 382,65 руб\n\"" +
                "Отклонений с планом не обнаружено");
        return v;
    }
}
