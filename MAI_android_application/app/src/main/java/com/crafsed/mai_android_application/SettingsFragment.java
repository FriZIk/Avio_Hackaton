package com.crafsed.mai_android_application;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.AlphaAnimation;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.fragment.app.Fragment;

public class SettingsFragment extends Fragment {
    Button mSaveButton;
    Button mCheckButton;
    TextView mResultTextView;
    TextView mSaveTextView;
    EditText mIpEditText;
    EditText mPortEditText;
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_settings, container, false);
        ActionBar actionBar = ((MainActivity)getActivity()).getSupportActionBar();
        actionBar.setTitle(getString(R.string.app_name)+" - Настройки");
        actionBar.setHomeButtonEnabled(true);
        actionBar.setDisplayHomeAsUpEnabled(true);
        final SharedPreferences sharedPreferences = getActivity().getSharedPreferences("SETTINGS", Context.MODE_PRIVATE);


        mSaveButton = v.findViewById(R.id.saveButton);
        mCheckButton = v.findViewById(R.id.checkButton);
        mResultTextView = v.findViewById(R.id.resultTextView);
        mSaveTextView = v.findViewById(R.id.saveTextView);
        mIpEditText = v.findViewById(R.id.IPEditView);
        mPortEditText = v.findViewById(R.id.portEditView);

        mSaveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!mIpEditText.getText().toString().isEmpty()&&!mPortEditText.getText().toString().isEmpty()) {
                    sharedPreferences.edit()
                            .putString("IP", mIpEditText.getText().toString())
                            .putInt("PORT", Integer.parseInt(mPortEditText.getText().toString()))
                            .apply();
                    animation(mSaveTextView);
                }
            }
        });

        mCheckButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                animation(mResultTextView);
            }
        });
        return v;
    }

    void checkCallBack(boolean result){
        AlphaAnimation animation = new AlphaAnimation(0.2f, 0.0f);
        animation.setDuration(400);
        animation.setStartOffset(0);
        animation.setFillAfter(true);
    }

    @Override
    public void onResume() {
        super.onResume();
        mIpEditText.setText(getActivity().getSharedPreferences("SETTINGS",Context.MODE_PRIVATE).getString("IP","0.tcp.ngrok.io"));
        mPortEditText.setText(String.valueOf(getActivity().getSharedPreferences("SETTINGS",Context.MODE_PRIVATE).getInt("PORT", 17748)));
    }

    void animation(View v){
        v.setAlpha(1);
        AlphaAnimation anim = new AlphaAnimation(1,0);
        anim.setDuration(5000);
        anim.setFillAfter(true);
        v.startAnimation(anim);
    }
}
