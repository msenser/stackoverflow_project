import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def plot_importance(df, countries=[]):
    '''
    INPUT
    df - pandas DataFrame
    countries - list of countries to consider, default=all

    OUTPUT
    plot of the importance of formal education to career for the selected counties
    '''

    #check if all counties should be considered, if yes, create a subset
    if len(countries)>0:
        df_c=df[df["Country"].isin(countries)]
    else:
        df_c=df
    #calculate distribution
    importance = df_c["NEWEdImpt"].value_counts()
    #rearrange data to fit into seaborn barplot
    df_importance=pd.DataFrame([importance.values],columns=importance.index.values)
    importance_order=['Critically important','Very important','Fairly important',  'Somewhat important',
       'Not at all important/not necessary' ]
    base_color = sb.color_palette()[0]
    #plot
    plot_importance=sb.barplot(data=df_importance, color = base_color, order = importance_order );
    plt.xticks(rotation=90) 
    imax=int(importance.max()*1.1)
    plt.ylim(0,imax)
    plot_importance.set(title='Importance of formal education to career')

    # print value on each bar
    i=0
    for col in importance_order:
        count = df_importance[col].iloc[0]
        plt.text(i, count+int(imax/15), count, ha = 'center', va='top')
        i+=1


def plot_job_seeking(df):
    '''
    INPUT
    df - pandas DataFrame

    OUTPUT
    plot of the job-seeking status
    '''

    #calculate distribution
    job_seeking = df["JobSeek"].value_counts()
    #rearrange data to fit into seaborn barplot
    df_job_seeking=pd.DataFrame([job_seeking.values],columns=job_seeking.index.values)
    job_seeking_order=['I am not interested in new job opportunities',
                      'I’m not actively looking, but I am open to new opportunities',
                      'I am actively looking for a job']
    base_color = sb.color_palette()[0]
    #plot
    plot_importance=sb.barplot(data=df_job_seeking, color = base_color, order = job_seeking_order );
    plt.xticks(rotation=90) 
    imax=int(job_seeking.max()*1.1)
    plt.ylim(0,imax)
    plot_importance.set(title='Importance of formal education to career')

    # print value on each bar
    i=0
    for col in job_seeking_order:
        count = df_job_seeking[col].iloc[0]
        plt.text(i, count+int(imax/15), count, ha = 'center', va='top')
        i+=1

def plot_company_size(df):
    '''
    INPUT
    df - pandas DataFrame

    OUTPUT
    plot of the different company sizes and distribution
    '''

    #calculate distribution
    org_size = df["OrgSize"].value_counts()
    #rearrange data to fit into seaborn barplot
    df_org_size=pd.DataFrame([org_size.values],columns=org_size.index.values)
    org_size_order = ['Just me - I am a freelancer, sole proprietor, etc.',
                    '2 to 9 employees', '10 to 19 employees','20 to 99 employees', '100 to 499 employees',
                    '500 to 999 employees',  '1,000 to 4,999 employees',
                    '5,000 to 9,999 employees','10,000 or more employees']     
    base_color = sb.color_palette()[0]
    #plot
    plot_importance=sb.barplot(data=df_org_size, color = base_color, order = org_size_order );
    plt.xticks(rotation=90) 
    imax=int(org_size.max()*1.1)
    plt.ylim(0,imax)
    plot_importance.set(title='Importance of formal education to career')

    # print value on each bar
    i=0
    for col in org_size_order:
        count = df_org_size[col].iloc[0]
        plt.text(i, count+int(imax/15), count, ha = 'center', va='top')
        i+=1