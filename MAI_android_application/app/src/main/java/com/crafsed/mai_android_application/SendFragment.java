package com.crafsed.mai_android_application;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.fragment.app.Fragment;

public class SendFragment extends Fragment{
    TextView mInformation;
    LoadFragment.MListener mMListener;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_loading, container, false);
        mInformation = v.findViewById(R.id.informationTextView);
        ActionBar actionBar = ((MainActivity)getActivity()).getSupportActionBar();
        actionBar.setTitle(getString(R.string.app_name)+" - Настройки");
        actionBar.setHomeButtonEnabled(true);
        actionBar.setDisplayHomeAsUpEnabled(true);
        mInformation.setText("Идет передача информации...");
        MyAsynkTask myAsynkTask = new MyAsynkTask();
        myAsynkTask.execute();
        return v;
    }

    class MyAsynkTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            Port.send(getActivity());
            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            mMListener.ok();
        }
    }
}
